from servo import rotate, init
from machine import Pin, PWM, ADC
from time import sleep
from ring_led import colorAll

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servoPin = Pin(26, Pin.OUT)
servo = PWM(servoPin, freq=500)
servo.deinit()
servo = PWM(servoPin, freq=500)

init(servo)
colorAll(255,0,0)

while True:
  analogVal = analogPin.read()
  rel_val = analogVal/MAX_ANALOG_VAL
  #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
  rotate(servo,rel_val)
  #sleep(0.001)
