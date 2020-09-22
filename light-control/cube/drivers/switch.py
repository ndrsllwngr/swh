from machine import Pin, PWM
from time import sleep

class SWITCH():

    def __init__(self, pin = 26):
        #pwm = PWM(Pin(pin), freq=500)
        #pwm.deinit()
        self.switch = Pin(pin, Pin.IN)

    def getValue(self):
        return self.switch.value()