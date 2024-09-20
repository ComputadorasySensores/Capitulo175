from machine import Pin, SoftI2C
from bh1750 import BH1750
import time

Relay = Pin(4, Pin.OUT)

i2c = SoftI2C(scl=Pin(9), sda=Pin(8), freq=400000)

sensor = BH1750(bus=i2c, addr=0x23)

while True:
    lux = sensor.luminance(BH1750.CONT_HIRES_1)
    print("Nivel: {:.2f} lux".format(lux))
    if (lux < 60):
        Relay.value(1)
    elif (lux > 80):
        Relay.value(0)
    time.sleep(2)
