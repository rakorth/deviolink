class SwitchConfig:
    def __init__(self, pin_num: str, status: bool):
        self.pin_num = pin_num
        self.status = status

    def to_dict(self):
        return {
            "pin_num": self.pin_num,
            "status": self.status
        }
