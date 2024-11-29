class NeopixelConfig:
    def __init__(self, pin_num, length):
        self.pin_num = pin_num
        self.length = length

    def to_dict(self):
        return {
            "pin_num": self.pin_num,
            "length": self.length
        }
