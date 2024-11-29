class ServoConfig:
    def __init__(self, scl_pin: str, sda_pin: str, channels: list[int]):
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.channels = channels

    def to_dict(self):
        return {
            'scl_pin': self.scl_pin,
            'sda_pin': self.sda_pin,
            'channels': self.channels
        }
