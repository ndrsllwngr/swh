from machine import Pin
from time import sleep_ms


class VibMotor():

    SHORT = 200
    LONG = 400

    def __init__(self, pin=5):
        self.motor = Pin(pin, Pin.OUT)

    def vibrate(self, time):
        self.motor.value(1)
        sleep_ms(time)
        self.motor.value(0)

    def vibrate_on(self):
        self.motor.value(1)

    def vibrate_short(self):
        self.vibrate(self.SHORT)

    def vibrate_long(self):
        self.vibrate(self.LONG)

    def vibrate_n(self, n, time=SHORT):
        for i in range(n):
            self.vibrate(time)
            sleep_ms(100)
