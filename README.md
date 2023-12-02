# Example of usage MicroPython on NodeMCU(ESP8266)

## Needed parts:
* NodeMCU;
* WS2812b;

1. Install esptool (https://github.com/espressif/esptool).
2. Download firmware for ESP8266 (http://micropython.org/download#esp8266).
3. Flash the board (example command bellow):
```esptool.py --port /dev/tty.wchusbserialfd120 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20180511-v1.9.4.bin```
4. Connect to the board and load these two files (you may use uPyCraft2).

5. Connect WS2812b to NodeMCU:
![Connection example](https://i.imgur.com/D0M5VyV.jpg)
6. Power on.
