from machine import Pin, ADC, PWM
from time import sleep

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

while True:
    analogVal = analogPin.read()
    rel_val = analogVal/MAX_ANALOG_VAL
    print("Analog: "+str(analogVal)+" - Brightness: "+str(100-rel_val*100)+"%")
    sleep(1)
