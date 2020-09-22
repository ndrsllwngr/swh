from machine import Pin
from time import sleep

class BUTTON():

    def __init__(self, pin = 26):
        self.button = Pin(pin, Pin.IN)

    def getValue(self):
        return self.button.value()