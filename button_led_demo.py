from machine import Pin
import time

dioda = Pin(5, Pin.OUT)
przycisk = Pin(4, Pin.IN, Pin.PULL_DOWN)

while True:
    if przycisk.value() == 0:
            dioda.value(1)
            time.sleep(0.5)
            dioda.value(0)
            time.sleep(0.5)
