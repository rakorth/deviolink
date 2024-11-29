from adafruit_httpserver import Websocket

import error_handler
from services import service_led_matrix, service_servo_motor, service_logging as log_factory, service_neopixel

logger = log_factory.create_logger("message_parser_binary")


# ==============================
#
# Binary message parser
# Responsible for converting raw binary websocket messages into service commands
#
# ==============================


def parse_binary_msg(websocket: Websocket, byte_arr: bytes):
    try:
        process_packet(byte_arr)
    except Exception as e:
        error_handler.handle_websocket_error(websocket, e)
        pass


def process_packet(packet):
    if len(packet) == 0:
        return

    command = packet[0]
    if command == 0:
        logger.debug("Echo packet")
    elif command == 2:
        process_servo_move_packet(packet)
    elif command == 3:
        process_ledmatrix_show_grid(packet)
    elif command == 4:
        process_ledmatrix_clear_grid(packet)
    elif command == 5:
        process_ledmatrix_warning_signal(packet)
    elif command == 6:
        process_ledmatrix_set_pixel_on(packet)
    elif command == 7:
        process_ledmatrix_set_pixel_off(packet)
    elif command == 9:
        process_neopixel_show_packet(packet)
    elif command == 10:
        process_neopixel_clear_packet(packet)
    elif command == 11:
        process_neopixel_fill_red_packet(packet)
    elif command == 12:
        process_neopixel_fill_green_packet(packet)
    elif command == 13:
        process_neopixel_fill_blue_packet(packet)
    elif command == 14:
        process_neopixel_set_color_packet(packet)
    else:
        logger.warning("Invalid command packet value: %d", command)


# Packet structure
# 0: int8  | static byte = 2
# 1: int8  | servo motor index
# 2: int8  | servo angle
def process_servo_move_packet(packet: list[int]):
    if len(packet) != 3:
        logger.warning("Invalid servo move packet length:%d expected 2", len(packet))
        return

    index = packet[1]
    angle = packet[2]
    service_servo_motor.set_servo_angle(index, angle)


# Packet structure
# 0: int8  | static byte = 3
# 1: int8  | matrix index
def process_ledmatrix_show_grid(packet: list[int]):
    if len(packet) != 2:
        raise InvalidPacketException(f"Invalid ledmatrix show packet length:%d expected 2", len(packet))
    service_led_matrix.show(packet[1])


# Packet structure
# 0: int8  | static byte = 4
# 1: int8  | matrix index
def process_ledmatrix_clear_grid(packet: list[int]):
    if len(packet) != 2:
        raise InvalidPacketException(f"Invalid ledmatrix clear packet length:%d expected 2", len(packet))
    service_led_matrix.clear(packet[1])


# Packet structure
# 0: int8  | static byte = 5
# 1: int8  | matrix index
def process_ledmatrix_warning_signal(packet: list[int]):
    if len(packet) != 2:
        raise InvalidPacketException(f"Invalid ledmatrix warning signal packet length:%d expected 2", len(packet))
    service_led_matrix.warning(packet[1])


# Packet structure
# 0: int8  | static byte = 6
# 1: int8  | matrix index
# 2: int16 | x value
# 3: int16 | x value
# 4: int16 | y value
# 5: int16 | y value
def process_ledmatrix_set_pixel_on(packet: list[int]):
    if len(packet) != 6:
        raise InvalidPacketException(f"Invalid ledmatrix set pixel on packet length:%d expected 6", len(packet))
    index = packet[1]
    x_pos = (packet[2] << 8) | packet[3]
    y_pos = (packet[4] << 8) | packet[5]

    service_led_matrix.set_pixel(index, x_pos, y_pos, True)


# Packet structure
# 0: int8  | static byte = 7
# 1: int8  | matrix index
# 2: int16 | x value
# 3: int16 | x value
# 4: int16 | y value
# 5: int16 | y value
def process_ledmatrix_set_pixel_off(packet: list[int]):
    if len(packet) != 6:
        raise InvalidPacketException(f"Invalid ledmatrix set pixel off packet length:%d expected 6", len(packet))
    index = packet[1]
    x_pos = (packet[2] << 8) | packet[3]
    y_pos = (packet[4] << 8) | packet[5]

    service_led_matrix.set_pixel(index, x_pos, y_pos, False)


# Packet structure
# 0: int8  | static byte = 9
# 1: int8  | hardware pin
def process_neopixel_show_packet(packet: list[int]):
    if len(packet) != 2:
        logger.warning("Invalid neopixel show packet length:%d expected 2", len(packet))
        return
    pin_num = packet[1]
    service_neopixel.show_strip(pin_num)


# Packet structure
# 0: int8  | static byte = 10
# 1: int8  | hardware pin
def process_neopixel_clear_packet(packet: list[int]):
    if len(packet) != 2:
        logger.warning(
            "Invalid neopixel clear packet length:%d expected 1", len(packet)
        )
        return
    pin_num = packet[1]
    service_neopixel.clear_strip(pin_num)


# Packet structure
# 0: int8  | static byte = 11
# 1: int8  | hardware pin
def process_neopixel_fill_red_packet(packet: list[int]):
    if len(packet) != 2:
        logger.warning(
            "Invalid neopixel fill red packet length:%d expected 1", len(packet)
        )
        return
    pin_num = packet[1]
    service_neopixel.fill_strip_red(pin_num)


# Packet structure
# 0: int8  | static byte = 12
# 1: int8  | hardware pin
def process_neopixel_fill_green_packet(packet: list[int]):
    if len(packet) != 2:
        logger.warning(
            "Invalid neopixel fill green packet length:%d expected 1", len(packet)
        )
        return
    pin_num = packet[1]
    service_neopixel.fill_strip_green(pin_num)


# Packet structure
# 0: int8  | static byte = 13
# 1: int8  | hardware pin
def process_neopixel_fill_blue_packet(packet: list[int]):
    if len(packet) != 2:
        logger.warning(
            "Invalid neopixel fill blue packet length:%d expected 1", len(packet)
        )
        return
    pin_num = packet[1]
    service_neopixel.fill_strip_blue(pin_num)


# Packet structure
# 0: int8  | static byte = 14
# 1: int8  | hardware pin
# 2: int16 | pixel index
# 3: int16 | pixel index
# 4: int8  | r color
# 5: int8  | g color
# 6: int8  | b color
def process_neopixel_set_color_packet(packet: list[int]):
    if len(packet) != 7:
        logger.warning(
            "Invalid neopixel set pixel color packet length:%d expected 7", len(packet)
        )
        return
    pin_num = packet[1]
    index = (packet[2] << 8) | packet[3]
    r = packet[4]
    g = packet[5]
    b = packet[6]

    service_neopixel.set_neopixel_color(pin_num, index, r, g, b)


class InvalidPacketException(Exception):
    pass
