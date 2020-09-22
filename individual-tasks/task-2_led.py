# ESP32
from machine import Pin
from time import sleep

led = Pin(26, Pin.OUT)  # external
# led = Pin(25, Pin.OUT) # internal

while True:  # blink led
    print("Blink")
    led.on()
    sleep(1)
    led.off()
    sleep(1)
