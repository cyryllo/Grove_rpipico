from machine import Pin, PWM

class SERVO:
    def __init__ (self,pin):
        self.pin = pin
        self.pwm = PWM(self.pin)

    def turn(self, val):
        self.pwm.freq(50)
        self.pwm.duty_u16(int(val/180*6000+1900))
