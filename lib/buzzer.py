from machine import Pin, PWM
from time import sleep
vol=100
po = 35
class Music:
    def __init__ (self,pin):
        self.pin = pin
        self.pwm = PWM(self.pin)
    
    def DO(self, vol):
        self.pwm.freq(1046) #DO
        self.pwm.duty_u16(vol*po)
    def RE(self, vol): 
        self.pwm.freq(1175) #RE
        self.pwm.duty_u16(vol*po)
    def MI(self, vol):        
        self.pwm.freq(1318) #MI
        self.pwm.duty_u16(vol*po)    
    def FA(self, vol):
        self.pwm.freq(1397) #FA
        self.pwm.duty_u16(vol*po)
    def SO(self, vol):
        self.pwm.freq(1568) #SO
        self.pwm.duty_u16(vol*po) 
    def LA(self, vol):   
        self.pwm.freq(1760) #LA
        self.pwm.duty_u16(vol*po)   
    def SI(self, vol): 
        self.pwm.freq(1967) #SI
        self.pwm.duty_u16(vol*po)
    def N(self):
        self.pwm.duty_u16(0)
