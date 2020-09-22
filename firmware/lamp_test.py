from drivers.servo import LAMP_SERVO
from machine import Pin, PWM, ADC
from time import sleep
from drivers.ring_led import colorAll

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servo = LAMP_SERVO()
colorAll(255,0,0)

while True:
  analogVal = analogPin.read()
  rel_val = analogVal/MAX_ANALOG_VAL
  #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
  servo.rotate(rel_val)
  sleep(0.01)
