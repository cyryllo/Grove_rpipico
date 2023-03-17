from machine import Pin,PWM
from buzzer import Music
from utime import sleep

mu = Music(Pin(27))

while True:
    mu.DO(100)
    sleep(1)
    mu.RE(50)
    sleep(1)  
    mu.MI(70)
    sleep(1)   
    mu.FA(40)
    sleep(1)  
    mu.SO(45)
    sleep(1)  
    mu.LA(60)
    sleep(1)
    mu.SI(100)
    sleep(1)
    mu.N()
    sleep(1)