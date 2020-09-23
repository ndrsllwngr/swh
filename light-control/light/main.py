from drivers.servo import LAMP_SERVO
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar, setNetVar
from util.colour import stringToInt

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")
lastColorStr = "0-0-0"

while True:

    reset = getNetVar("lampReset")
    if reset == 'True':
        setNetVar("lampReset", False)
        import machine
        machine.reset()

    position = float(getNetVar("lampPosition"))
    servo.rotate(position)
    
    colors = stringToInt(getNetVar("lampColour"))
    colorStr = str(colors)
    print("Pos: "+str(position)+" Color: "+colorStr)
    if colorStr != lastColorStr:
        ring_led.colorAll(colors[0], colors[1], colors[2])
        print("New Color: "+colorStr)
        lastColorStr = colorStr
    sleep_ms(10)
