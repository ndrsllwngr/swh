from machine import Pin, PWM
from time import sleep

# connect it to Pin 26, 27, and 14
blue = PWM(Pin(14))
green = PWM(Pin(12))
red = PWM(Pin(26))

# base frequency for PWM is 1000Hz
blue.freq(1000)
green.freq(1000)
red.freq(1000)


def rgb(r=255, g=255, b=255):
    blue.duty(b*4)          # set duty cycle
    green.duty(g*4)          # set duty cycle
    red.duty(r*4)          # set duty cycle


# show some cases....
i = 0
while True:
    rgb(255, 255, 255)  # white
    sleep(1)
    rgb(0, 0, 0)  # off = black
    sleep(1)
    rgb(255, 0, 0)  # red
    sleep(1)
    rgb(0, 255, 0)  # gree
    sleep(1)
    rgb(0, 0, 255)  # blue
    sleep(1)
    rgb(100, 100, 100)
    sleep(1)
    rgb(150, 150, 150)
    sleep(1)
    rgb(200, 200, 200)
    sleep(1)
    rgb(50, 150, 250)
    sleep(1)
    rgb(250, 150, 50)
    i = i+1
    rgb(1+i, 100+8*i, 50+2*i)
