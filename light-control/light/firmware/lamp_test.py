from drivers.servo import LAMP_SERVO
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import colorAll
from util.netvars import initNet, getNetVar

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servo = LAMP_SERVO()

initNet("Wu-Tang-Lan", "doppelhure69")
colorAll(255,0,0)

while True:
  #analogVal = analogPin.read()
  #rel_val = analogVal/MAX_ANALOG_VAL
  #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
  position = float(getNetVar("lampPosition"))
  print("New Position: "+str(position))
  servo.rotate(position)
  sleep_ms(10)
