from drivers.servo import LAMP_SERVO
import utime
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar, setNetVar
from util.colour import stringToInt

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")
lastColorStr = "0-0-0"
lastUpdated = utime.time()

while True:
    try:
        timeDiff = utime.time() - lastUpdated
        if timeDiff > 30:
            lastUpdated = utime.time()
            print("OUCH!")
            reset = getNetVar("lampReset")
            if reset == 'True':
                setNetVar("lampReset", False)
                import machine
                machine.reset()
    
        position = float(getNetVar("lampPosition"))
        servo.rotate(position)
        
        colors = stringToInt(getNetVar("lampColour"))
        colorStr = str(colors)
        print("Pos: "+str(position)+" Color: "+colorStr+" TimeDiff: "+str(timeDiff))
        if colorStr != lastColorStr:
            ring_led.colorAll(colors[0], colors[1], colors[2])
            print("New Color: "+colorStr)
            lastColorStr = colorStr
        sleep_ms(30)
    except OSError :
        print("Caught an OSError")
        continue

