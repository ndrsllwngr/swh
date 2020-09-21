from servo_util import rotate, init
from machine import Pin, PWM, ADC
from time import sleep

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servoPin = Pin(26, Pin.OUT)
servo = PWM(servoPin, freq=500)
servo.deinit()
servo = PWM(servoPin, freq=500)

init(servo)


while True:
  analogVal = analogPin.read()
  rel_val = analogVal/MAX_ANALOG_VAL
  #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
  rotate(servo,rel_val)
  #sleep(0.001)
