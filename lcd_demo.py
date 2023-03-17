from lcd1602 import LCD1602
from machine import I2C,Pin
from utime import sleep
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16) 
ja = "Cyryl"
d.display() 
sleep(1)
d.clear()
d.print('Witaj '+ ja) 

sleep(1)
d.setCursor(0, 1)
d.print('w FabLabie! ')