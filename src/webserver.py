from asyncio import create_task, gather, run, sleep as async_sleep

import microcontroller
import socketpool
import wifi
from adafruit_httpserver import Server, Websocket, GET, POST, Route, PUT

from controllers import controller_logging, controller_system, controller_health, controller_websocket
import message_parser_binary
import message_parser_string

### --------------------------------------
### Webserver loop
###
### Ref: https://docs.circuitpython.org/projects/httpserver/en/latest/api.html#
### Ref: https://learn.adafruit.com/networking-in-circuitpython/http-server-examples
### --------------------------------------


pool = socketpool.SocketPool(wifi.radio)
server = Server(pool)
websocket: Websocket = None


async def handle_http_requests():
    while True:
        server.poll()
        microcontroller.watchdog.feed()
        await async_sleep(0)


async def handle_websocket_requests():
    while True:
        try:
            if websocket is not None:
                if (data := websocket.receive(fail_silently=True)) is not None:
                    if isinstance(data, str):
                        message_parser_string.parse_string_msg(websocket, data)
                    else:
                        message_parser_binary.parse_binary_msg(websocket, data)
        except:
            # Websocket read errors can still occur even if fail_silently is true
            # try/catch is to keep loop running
            pass

        microcontroller.watchdog.feed()
        await async_sleep(0)


async def async_webserver():
    await gather(
        create_task(handle_http_requests()),
        create_task(handle_websocket_requests()),
        create_task(controller_websocket.websocket_heartbeat_msg()),
    )


def start_webserver():
    server.start(str(wifi.radio.ipv4_address))
    server.add_routes([
        Route("/logs", GET, controller_logging.logging_details_endpoint),
        Route("/logs", PUT, controller_logging.update_logging_level),

        Route("/health", GET, controller_health.health_endpoint),

        Route("/info", GET, controller_system.system_info_endpoint),

        Route("/config", GET, controller_system.get_device_config_endpoint),
        Route("/config/update", POST, controller_system.update_system_config_endpoint),

        Route("/websocket", GET, controller_websocket.create_websocket_connection)
    ])
    run(async_webserver())
