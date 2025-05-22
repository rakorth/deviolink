import busio
import digitalio

from services import service_logging as log_factory
import utils_pins as p

# ==============================
#
# Led Matrix service
#
# ==============================

logger = log_factory.create_logger("switch_controller")

pins = []


def add_switch(switch_pin: str, status: bool = False):
    logger.info("Switch: Adding switch on pin:%s", switch_pin)
    pin = p.get_board_pin(switch_pin)
    switch = digitalio.DigitalInOut(pin)
    pins.append(switch)
    set_switch(len(pins) - 1, status)


def set_switch(index: int, status: bool):
    logger.info("Switch: %d set to %s", index, status)
    switch = pins[index]
    switch.value = status
