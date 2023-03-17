from ws2812 import WS2812
import utime

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

led = WS2812(20,16)#WS2812(pin_num,led_count)
led.rainbow_cycle(0)
utime.sleep(2)

print("chases")
for color in COLORS:
    led.color_chase(color, 0.01)

while True:
    print("fills")
    for color in COLORS: 
        led.pixels_fill(color)
        led.pixels_show()
        utime.sleep(0.2)