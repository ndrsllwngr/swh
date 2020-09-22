# ESP32
from machine import Pin
from time import sleep

red = Pin(26, Pin.OUT)
green = Pin(12, Pin.OUT)
blue = Pin(14, Pin.OUT)

while True:  # blink led
    print("blue")
    blue.on()
    green.off()
    red.off()
    sleep(1)
    print("green")
    blue.off()
    green.on()
    red.off()
    sleep(1)
    print("red")
    blue.off()
    green.off()
    red.on()
    sleep(1)
