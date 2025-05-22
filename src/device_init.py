import adafruit_logging as logging

import webserver
from logging_handler_websocket import WebsocketHandler
from services import service_system, service_led_matrix, service_servo_motor, service_logging as log_factory, \
    service_neopixel, service_switch

logger = log_factory.create_logger("device_init_service")


def init_device() -> None:
    logger.info("Device is initializing")
    try:
        for log_name in log_factory.get_logger_names():
            l = logging.getLogger(log_name)
            l.addHandler(WebsocketHandler())  ## Websockets
            l.addHandler(logging.StreamHandler())  ## Stdio

        _configure_devices()

        service_system.SYSTEM_IS_SAFE_MODE = False
        logger.info("Device is in run mode")
    except Exception as ex:
        service_system.SYSTEM_IS_SAFE_MODE = True
        service_system.SYSTEM_SAFE_MODE_ERR_MESSAGE = str(ex)
        logger.info("Device is in safe mode: %s", ex)

    webserver.start_webserver()


def _configure_devices():
    device_config = service_system.get_device_config()

    for config in device_config.led_matrix_configs:
        service_led_matrix.add_matrix(config.clock_pin, config.mosi_pin, config.chip_select_pin, config.width,
                                      config.height)

    for neo_config in device_config.neopixel_configs:
        service_neopixel.add_pixel_strip(neo_config.pin_num, neo_config.length)

    for servo_config in device_config.servo_configs:
        service_servo_motor.add_i2c_servo_controller(servo_config.scl_pin, servo_config.sda_pin, servo_config.channels)

    for switch_config in device_config.switch_configs:
        service_switch.add_switch(switch_config.pin_num, switch_config.status)