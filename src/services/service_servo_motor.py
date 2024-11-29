import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

from services import service_logging as log_factory
import utils_pins as p

# ==============================
#
# Servo service
#
# Ref: https://www.adafruit.com/product/2201
# ==============================

logger = log_factory.create_logger("servo_controller")

servos = {}


def add_i2c_servo_controller(scl_pin: str, sda_pin: str, channels: list[int]):
    logger.info("Servo: Creating servo controller with scl:%s sda:%s", scl_pin, sda_pin)
    scl = p.get_board_pin(scl_pin)
    sda = p.get_board_pin(sda_pin)

    i2c = busio.I2C(scl=scl, sda=sda)
    pca = PCA9685(i2c, address=0x40, reference_clock_speed=25630710)
    pca.frequency = 50

    for channel in channels:
        s = servo.Servo(pca.channels[channel], min_pulse=580, max_pulse=2350)
        servos[channel] = s


def set_servo_angle(index: int, angle: int):
    logger.info("Servo: %d setting angle %d", index, angle)
    servos[index].angle = angle
