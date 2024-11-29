# ==============================
#
# Neopixel service
#
# ==============================
import neopixel

from services import service_logging as log_factory
import utils_pins as p

logger = log_factory.create_logger("neopixel_controller")

neopixel_list = []


def add_pixel_strip(pin_str: str, length: int):
    """
    add a neopixel strip to the service
    will blank out strip on create
    :param pin_str: string representation of pin ie: IO9, GP04
    :param length: total num of neopixel pixels in strip
    """
    pin = p.get_board_pin(pin_str)
    strip = neopixel.NeoPixel(pin, length, auto_write=False)

    neopixel_list.append(strip)
    logger.info("Neopixel: Add strip on pin:%s with length:%d", pin_str, length)
    strip.fill((0, 0, 0))
    strip.show()


def show_strip(strip_index: int):
    """
    Displays all buffered neopixel values in strip
    :param strip_index: index of the neopixel strip in neopixel_list
    """
    np = _get_neopixel_strip(strip_index)
    logger.debug("Neopixel:[%d] Show", strip_index)
    np.show()


def clear_strip(strip_index: int):
    """
    Clears entire neopixel strip
    :param strip_index: index of the neopixel strip in neopixel_list
    """
    np = _get_neopixel_strip(strip_index)
    logger.debug("Neopixel:[%d] Clear", strip_index)
    np.fill((0, 0, 0))
    np.show()


def fill_strip_red(strip_index: int):
    """
    Set entire neopixel strip to red
    :param strip_index: index of the neopixel strip in neopixel_list
    """
    np = _get_neopixel_strip(strip_index)
    logger.debug("Neopixel:[%d] Filling red", strip_index)
    np.fill((255, 0, 0))
    np.show()


def fill_strip_green(strip_index: int):
    """
    Set entire neopixel strip to green
    :param strip_index: index of the neopixel strip in neopixel_list
    """
    np = _get_neopixel_strip(strip_index)
    logger.debug("Neopixel:[%d] Filling green", strip_index)
    np.fill((0, 255, 0))
    np.show()


def fill_strip_blue(strip_index: int):
    """
    Set entire neopixel strip to blue
    :param strip_index: index of the neopixel strip in neopixel_list
    """
    np = _get_neopixel_strip(strip_index)
    logger.debug("Neopixel:[%d] Filling blue", strip_index)
    np.fill((0, 0, 255))
    np.show()


def set_neopixel_color(strip_index: int, pixel_index: int, r: int, g: int, b: int):
    """
    Set the color of the neopixel on a strip
    :param strip_index: index of the neopixel strip in neopixel_list
    :param pixel_index: index of the neopixel pixel in strip
    :param r: rgb - red value (0-255)
    :param g: rgb - green value (0-255)
    :param b: rgb - blue value (0-255)
    :return: null
    """
    np = _get_neopixel_strip(strip_index)

    if np.n <= pixel_index:
        logger.warning("Neopixel:[%d] Invalid pixel index:%d", strip_index, pixel_index)
        return

    logger.debug("Neopixel:[%d] #%d set color(%d, %d, %d)", strip_index, pixel_index, r, g, b)
    np[pixel_index] = (r, g, b)


def _get_neopixel_strip(strip_index: int) -> neopixel.NeoPixel:
    """
    Get the neopixel strip from the internal array or throw a value error if index is invalid
    :param strip_index: index of the neopixel strip in neopixel_list
    :return: neopixel strip
    """
    strip = neopixel_list[strip_index]
    if strip is not None:
        return strip
    raise ValueError(f"{strip_index} is not a valid neopixel strip")
