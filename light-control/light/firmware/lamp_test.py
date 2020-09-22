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
ring_led.colorAll(255,0,0)

while True:
  #analogVal = analogPin.read()
  #rel_val = analogVal/MAX_ANALOG_VAL
  #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
  position = float(getNetVar("lampPosition"))
  print("New Position: "+str(position))
  servo.rotate(position)
  
  colors = stringToInt(getNetVar("lampColour"))
  print("New Color: "+str(colors))

  sleep_ms(10)
