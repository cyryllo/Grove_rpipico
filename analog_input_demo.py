from machine import ADC, Pin
import time

analog = ADC(Pin(26))

while True:
    print(analog.read_u16())
    time.sleep(0.5)
