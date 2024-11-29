import json
from asyncio import sleep as async_sleep

from adafruit_httpserver import Request, Websocket

import webserver
from services import service_system


### --------------------------------------
### Controller for websockets
### --------------------------------------

def create_websocket_connection(request: Request):
    if webserver.websocket is not None:
        webserver.websocket.close()  # Close any existing connection

    webserver.websocket = Websocket(request, buffer_size=2048)

    return webserver.websocket


async def websocket_heartbeat_msg():
    while True:
        if webserver.websocket is not None:
            response = json.dumps(service_system.get_hardware_status())
            webserver.websocket.send_message(str(response), fail_silently=True)
        await async_sleep(10)
