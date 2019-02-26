import neopixel, machine
import gc


np = neopixel.NeoPixel(machine.Pin(2), 20)
gc.collect()
