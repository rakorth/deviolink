class LedMatrixConfig:
    def __init__(self, clock_pin: str, mosi_pin: str, chip_select_pin: str, width: int, height: int):
        self.clock_pin = clock_pin
        self.mosi_pin = mosi_pin
        self.chip_select_pin = chip_select_pin
        self.width = width
        self.height = height

    def to_dict(self) -> dict:
        return {
            "clock_pin": self.clock_pin,
            "mosi_pin": self.mosi_pin,
            "chip_select_pin": self.chip_select_pin,
            "width": self.width,
            "height": self.height
        }
