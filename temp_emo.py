from machine import Pin, I2C
import utime as time
from dht11 import DHT11, InvalidChecksum

time.sleep(1)
pin = Pin(18, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
t  = (sensor.temperature)
h = (sensor.humidity)
print("Temperature: {}".format(sensor.temperature))
print("Humidity: {}".format(sensor.humidity))