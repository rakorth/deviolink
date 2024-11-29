import busio
import digitalio
from adafruit_max7219 import matrices

from services import service_logging as log_factory
import utils_pins as p

# ==============================
#
# Led Matrix service
#
# ==============================

logger = log_factory.create_logger("led_matrix_controller")

matrix_list = []


def add_matrix(clock_pin: str, mosi_pin: str, chip_select_pin: str, width: int, height: int):
    """
    Add a matrix to the service
    :param clock_pin:
    :param mosi_pin:
    :param chip_select_pin:
    :param width:
    :param height:
    """
    p1 = p.get_board_pin(clock_pin)
    p2 = p.get_board_pin(mosi_pin)
    p3 = p.get_board_pin(chip_select_pin)

    spi = busio.SPI(clock=p1, MOSI=p2)
    cs = digitalio.DigitalInOut(p3)
    matrix = matrices.CustomMatrix(spi, cs, width, height)

    device = LedMatrixDevice(spi, cs, matrix, width, height)
    matrix_list.append(device)


def clear(index: int):
    """
    Clears LED Matrix display
    :param index: index of the LED matrix in matrix_list
    """
    logger.info("index:%d clear", index)
    matrix = _get_matrix(index)
    matrix.fill(False)
    matrix.show()


def set_pixel(index: int, x: int, y: int, status: bool):
    """
    Set individual pixel on a LED matrix to ON or OFF
    :param index: index of the LED matrix in matrix_list
    :param x:
    :param y:
    :param status:
    """
    logger.debug("LED: %d-%d %s", x, y, status)
    matrix = _get_matrix(index)
    if status:
        matrix.pixel(x, y, 1)
    else:
        matrix.pixel(x, y, 0)


def show(index: int):
    """
    Display buffered values to hardware matrix
    :param index: index of the LED matrix in matrix_list
    """
    logger.info("LED: show")
    matrix = _get_matrix(index)
    matrix.show()


def warning(index: int):
    """
    Display !'s all along the led matrix
    :param index:
    """
    logger.info("LED: warning")
    matrix = _get_matrix(index)
    matrix.fill(False)

    for c in range(8):
        i = (c * 4) + 1
        matrix.pixel(i, 1, True)
        matrix.pixel(i, 2, True)
        matrix.pixel(i, 3, True)
        matrix.pixel(i, 4, True)
        matrix.pixel(i, 6, True)

    matrix.show()


def _get_matrix(index: int) -> matrices.CustomMatrix:
    device = matrix_list[index]
    return device.matrix


class LedMatrixDevice:
    def __init__(self, spi: busio.SPI, cs: digitalio.DigitalInOut, matrix: matrices.CustomMatrix, width: int,
                 height: int):
        self.spi = spi
        self.cs = cs
        self.matrix = matrix
        self.width = width
        self.height = height
