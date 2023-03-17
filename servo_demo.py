from machine import Pin
from utime import sleep
from servo import SERVO
servo = SERVO(Pin(20))

for i in range(10):
    servo.turn(0)
    print(0)
    sleep(1)
    
    servo.turn(180)
    print(1)
    sleep(1)