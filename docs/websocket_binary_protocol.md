# Binary websocket protocol

Written to reduce data transmission size when sending messages to deviolink board

---

### Echo Packet

| byte index | size | type   | description  | value |
|------------|------|--------|--------------|-------|
| 0          | int8 | static | Command Byte | 0     |

---

### Move Servo Packet

| byte index | size | type    | description          | value |
|------------|------|---------|----------------------|-------|
| 0          | int8 | static  | Command Byte         | 2     |
| 1          | int8 | dynamic | index of servo motor |       |
| 2          | int8 | dynamic | angle value: 0-180   |       |

Moves a servo to a specified degree
index is determined by order of `channels` in the `servo_configs` in `device-config`

---

### Show Led Matrix Packet

| byte index | size | type    | description         | value |
|------------|------|---------|---------------------|-------|
| 0          | int8 | static  | Command Byte        | 3     |
| 1          | int8 | dynamic | index of led matrix |       |

Displays all cached matrix pixels  
index is determined by order of `led_matrix_configs` in `device-config`

---

### Clear Led Matrix Packet

| byte index | size | type    | description         | value |
|------------|------|---------|---------------------|-------|
| 0          | int8 | static  | Command Byte        | 4     |
| 1          | int8 | dynamic | index of led matrix |       |

Clears all pixels in a led matrix
index is determined by order of `led_matrix_configs` in `device-config`

---

### Warning Led Matrix Packet

| byte index | size | type    | description         | value |
|------------|------|---------|---------------------|-------|
| 0          | int8 | static  | Command Byte        | 5     |
| 1          | int8 | dynamic | index of led matrix |       |

Display !'s all along the led matrix
index is determined by order of `led_matrix_configs` in `device-config`

---

### Set Led Matrix Pixel On Packet

| byte index | size  | type    | description         | value |
|------------|-------|---------|---------------------|-------|
| 0          | int8  | static  | Command Byte        | 6     |
| 1          | int8  | dynamic | index of led matrix |       |
| 2          | int16 | dynamic | x value             |       |
| 3          | ---   | ----    | -----               |       |
| 4          | int16 | dynamic | y value             |       |
| 5          | ---   | ----    | -----               |       |

Set individual pixel on a LED matrix to ON
index is determined by order of `led_matrix_configs` in `device-config`

---

### Set Led Matrix Pixel Off Packet

| byte index | size  | type    | description         | value |
|------------|-------|---------|---------------------|-------|
| 0          | int8  | static  | Command Byte        | 7     |
| 1          | int8  | dynamic | index of led matrix |       |
| 2          | int16 | dynamic | x value             |       |
| 3          | ---   | ----    | -----               |       |
| 4          | int16 | dynamic | y value             |       |
| 5          | ---   | ----    | -----               |       |

Set individual pixel on a LED matrix to OFF
index is determined by order of `led_matrix_configs` in `device-config`

---

### Show Neopixel Packet

| byte index | size | type    | description             | value |
|------------|------|---------|-------------------------|-------|
| 0          | int8 | static  | Command Byte            | 9     |
| 1          | int8 | dynamic | index of neopixel strip |       |

Displays all cached neopixels in strip
index is determined by order of `neopixel_configs` in `device-config`

---

### Clear Neopixel Packet

| byte index | size | type    | description             | value |
|------------|------|---------|-------------------------|-------|
| 0          | int8 | static  | Command Byte            | 10    |
| 1          | int8 | dynamic | index of neopixel strip |       |

Clears all colors neopixels in strip
index is determined by order of `neopixel_configs` in `device-config`

---

### Fill Neopixel Strip To Red Packet

| byte index | size | type    | description             | value |
|------------|------|---------|-------------------------|-------|
| 0          | int8 | static  | Command Byte            | 11    |
| 1          | int8 | dynamic | index of neopixel strip |       |

Sets all neopixels in strip to 255,0,0
index is determined by order of `neopixel_configs` in `device-config`

---

### Fill Neopixel Strip To Green Packet

| byte index | size | type    | description             | value |
|------------|------|---------|-------------------------|-------|
| 0          | int8 | static  | Command Byte            | 12    |
| 1          | int8 | dynamic | index of neopixel strip |       |

Sets all neopixels in strip to 0,255,0
index is determined by order of `neopixel_configs` in `device-config`

---

### Fill Neopixel Strip To Blue Packet

| byte index | size | type    | description             | value |
|------------|------|---------|-------------------------|-------|
| 0          | int8 | static  | Command Byte            | 13    |
| 1          | int8 | dynamic | index of neopixel strip |       |

Sets all neopixels in strip to 0,0,255
index is determined by order of `neopixel_configs` in `device-config`

---

### Set Neopixel Color Packet

| byte index | size  | type    | description             | value |
|------------|-------|---------|-------------------------|-------|
| 0          | int8  | static  | Command Byte            | 14    |
| 1          | int8  | dynamic | index of neopixel strip |       |
| 2          | int16 | dynamic | pixel index             |       |
| 3          | ---   | ----    | -----                   |       |
| 4          | int8  | dynamic | red value 0-255         |       |
| 5          | int8  | dynamic | green value 0-255       |       |
| 6          | int8  | dynamic | blue value 0-255        |       |

Sets individual neopixel in strip to rgb value
index is determined by order of `neopixel_configs` in `device-config`

---

### Set Switch On

| byte index | size  | type    | description       | value |
|------------|-------|---------|-------------------|-------|
| 0          | int8  | static  | Command Byte      | 15    |
| 1          | int8  | dynamic | index of pin      |       |

---

### Set Switch Off

| byte index | size  | type    | description       | value |
|------------|-------|---------|-------------------|-------|
| 0          | int8  | static  | Command Byte      | 16    |
| 1          | int8  | dynamic | index of pin      |       |







