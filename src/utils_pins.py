import board


def get_board_pin(pin_name: str):
    """
    Convert a string pin name to a board pin object.
    Example: get_board_pin('LED') returns board.LED
    Example: get_board_pin('D13') returns board.D13
    Example: get_board_pin('GP0') returns board.GP0

    Args:
        pin_name (str): Name of the pin (e.g. 'LED', 'D13', 'GP0')

    Returns:
        board pin object or None if pin doesn't exist
    """
    try:
        # Convert pin name to uppercase to match board attributes
        pin_name = pin_name.upper()

        # Get the pin from the board module if it exists
        if hasattr(board, pin_name):
            return getattr(board, pin_name)

        # Pin wasn't found
        print(f"Warning: Pin {pin_name} not found on this board")
        return None
    except Exception as e:
        print(f"Error getting pin {pin_name}: {str(e)}")
        return None


def list_available_pins():
    available_pins = []
    for attribute in dir(board):
        # Only include pin attributes (typically uppercase)
        if attribute.isupper():
            available_pins.append(attribute)
    return available_pins
