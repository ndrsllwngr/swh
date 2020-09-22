from drivers.servo import LAMP_SERVO
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar
from util.colour import stringToInt

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")
lastColorStr = "0-0-0"

while True:
    #analogVal = analogPin.read()
    #rel_val = analogVal/MAX_ANALOG_VAL
    #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
    position = float(getNetVar("lampPosition"))
    servo.rotate(position)
    print("New Position: "+str(position))
    
    colors = stringToInt(getNetVar("lampColour"))
    colorStr = str(colors)
    if colorStr != lastColorStr:
        ring_led.colorAll(colors[0], colors[1], colors[2])
        print("New Color: "+colorStr)
        lastColorStr = colorStr
    sleep_ms(10)
