import gc
import json
import os

import microcontroller

import constants
from views.config_device import DeviceConfig
from views.config_led_matrix import LedMatrixConfig
from views.config_neopixel import NeopixelConfig
from views.config_servo import ServoConfig
from views.view_system_info import SystemInfoView

#
# Service to get hardware status and read values out of settings.toml and device_config.json
#

SYSTEM_IS_SAFE_MODE = True
SYSTEM_SAFE_MODE_ERR_MESSAGE: str = ""
DEVICE_CONFIG = None


def get_device_config() -> DeviceConfig:
    global DEVICE_CONFIG
    if DEVICE_CONFIG is None:
        DEVICE_CONFIG = _load_device_config_from_filesystem()
    return DEVICE_CONFIG


def save_device_config(config: DeviceConfig) -> DeviceConfig:
    with open("../device_config.json", "w") as file:
        file.write(json.dumps(config))
    return config


def get_hardware_status() -> dict:
    return {
        constants.SYS_HEALTH_CPU_TEMP: round(microcontroller.cpu.temperature, 2),
        constants.SYS_HEALTH_CPU_FREQ: microcontroller.cpu.frequency,
        constants.SYS_HEALTH_MEM_USED: gc.mem_alloc(),
        constants.SYS_HEALTH_MEM_TOTAL: gc.mem_alloc() + gc.mem_free(),
    }


def get_system_info() -> SystemInfoView:
    return SystemInfoView(
        software_type=os.getenv(constants.SETTINGS_SOFTWARE_TYPE),
        software_version=os.getenv(constants.SETTINGS_SOFTWARE_VERSION),
        hardware_device_id=microcontroller.cpu.uid.hex(),
        device_config_name=DEVICE_CONFIG.device_name if DEVICE_CONFIG is not None else "?? Device is in safe mode ??",
        in_safe_mode=SYSTEM_IS_SAFE_MODE,
        safe_mode_err_msg=SYSTEM_SAFE_MODE_ERR_MESSAGE
    )


def _load_device_config_from_filesystem() -> DeviceConfig:
    with open("../device_config.json", "r") as file:
        try:
            # Parse JSON string into dictionary
            config_dict = json.load(file)

            # Parse LED matrix configurations
            led_matrix_configs = []
            for matrix_config in config_dict.get("led_matrix_configs", []):
                led_matrix = LedMatrixConfig(
                    clock_pin=matrix_config["clock_pin"],
                    mosi_pin=matrix_config["mosi_pin"],
                    chip_select_pin=matrix_config["chip_select_pin"],
                    width=matrix_config["width"],
                    height=matrix_config["height"]
                )
                led_matrix_configs.append(led_matrix)

            # Parse NeoPixel configurations
            neopixel_configs = []
            for pixel_config in config_dict.get("neopixel_configs", []):
                neopixel = NeopixelConfig(
                    pin_num=pixel_config["pin_num"],
                    length=pixel_config["length"]
                )
                neopixel_configs.append(neopixel)

            # Parse Servo configurations
            servo_configs = []
            for servo_config in config_dict.get("servo_configs", []):
                servo = ServoConfig(
                    scl_pin=servo_config["scl_pin"],
                    sda_pin=servo_config["sda_pin"],
                    channels=servo_config["channels"]
                )
                servo_configs.append(servo)

            # Create and return the DeviceConfig object
            return DeviceConfig(
                device_name=config_dict["device_name"],
                led_matrix_configs=led_matrix_configs,
                neopixel_configs=neopixel_configs,
                servo_configs=servo_configs,
            )

        except KeyError as e:
            raise ValueError(f"Missing required field in configuration: {str(e)}")
        except Exception as e:

            raise ValueError(f"Invalid JSON string: {str(e)}")
