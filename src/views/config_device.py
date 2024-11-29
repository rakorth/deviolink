from views.config_led_matrix import LedMatrixConfig
from views.config_neopixel import NeopixelConfig
from views.config_servo import ServoConfig


class DeviceConfig:
    def __init__(self, device_name: str, led_matrix_configs: list[LedMatrixConfig],
                 neopixel_configs: list[NeopixelConfig], servo_configs: list[ServoConfig]):
        self.device_name = device_name
        self.led_matrix_configs = led_matrix_configs
        self.neopixel_configs = neopixel_configs
        self.servo_configs = servo_configs

    def to_dict(self):
        return {
            'device_name': self.device_name,
            'led_matrix_configs': [config.to_dict() for config in self.led_matrix_configs],
            'neopixel_configs': [config.to_dict() for config in self.neopixel_configs],
            'servo_configs': [config.to_dict() for config in self.servo_configs]
        }
