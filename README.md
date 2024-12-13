# deviolink

<!-- TOC -->
* [deviolink](#deviolink)
  * [Device Setup](#device-setup)
  * [Documentation](#documentation)
  * [Python Libs](#python-libs)
  * [Development](#development)
    * [Testing](#testing)
    * [Windows Development - Pycharm](#windows-development---pycharm)
<!-- TOC -->
CircuitPython project for controlling hardware components via websocket / rest interfaces

Currently Supports:
* NeoPixels / WS2812 
* Led Matrix's using the MAX7219 chipset
* Servo motors vis I2C with a PCA9685 driver

## Device Setup

* [Find your board on the Circuit Python website](https://circuitpython.org/downloads)
* Install CircuitPython 9.x.x
* Copy contents of `src/` folder to root folder of the `CIRCUITPY` filesystem
* Update `settings.toml` with Wi-Fi ssid and password
* Create a `device_config.json` file with configs for all connected components. The `device_config.json` should be saved
  in root folder of the `CIRCUITPY` filesystem. An example json file can be found in `docs/example_device_config.json`

## Documentation

* Openapi spec for all http endpoints can be found in `docs/openapi.json`
* Binary protocol for websockets can be found in `docs/websocket_binary_protocol.md` and `src/message_parser_binary.py`
* Json schema and docs for how `device_config.json` should be structured can be found in
  `docs/device_config_schema.json`

## Python Libs

* circuitpython-stubs
* adafruit-circuitpython-logging
* adafruit-circuitpython-httpserver
* adafruit-circuitpython-motor
* adafruit-circuitpython-pca9685
* adafruit-circuitpython-neopixel
* adafruit-circuitpython-max7219

## Development

### Testing

| Board                   | Status  | Notes                |
|-------------------------|---------|----------------------|
| Waveshare ESP32-S3-Zero | Working | Main board tested on |
| Pico W                  | Working |                      |

### Windows Development - Pycharm

Setting up a symlink between your circuit-python device and `src/` folder makes it easier to develop on device while
utilizing pycharm features.

Example: Will link G: drive to src/ folder

```commandline
mklink /J %cd%\src G:\
```
