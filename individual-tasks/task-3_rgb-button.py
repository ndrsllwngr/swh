from machine import Pin, PWM
from time import sleep

buttonPin = Pin(25, Pin.IN)

MAX_ANALOG_VAL = 4095

# connect it to Pin 26, 27, and 14
blue = PWM(Pin(27))
green = PWM(Pin(12))
red = PWM(Pin(13))

# intensity not higher than 4


def rgb(r=255, g=255, b=255, intensity=1.0):
    if intensity > 1:
        intensity = 1
    intensity = 4*intensity
    blue.duty(int(b*intensity))
    green.duty(int(g*intensity))
    red.duty(int(r*intensity))


while True:
    buttonVal = buttonPin.value()
    rgb(255, 255, 255, buttonVal)
    print("ButtonVal: "+str(buttonVal))
    sleep(0.3)
