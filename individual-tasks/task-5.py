from machine import Pin, ADC
from time import sleep

analogPin = ADC(Pin(36))
analogPin.atten(ADC.ATTN_11DB)

p4 = machine.Pin(12)
servo = machine.PWM(p4, freq=50)

while True:
    analogVal = analogPin.read()
    print(analogVal)
    sleep(0.2)
    servo.duty(int(analogVal/35))
