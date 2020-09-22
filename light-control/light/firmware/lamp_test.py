from drivers.servo import LAMP_SERVO
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar
from util.colour import stringToInt
import socket

analogPin = ADC(Pin(34))
analogPin.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")


s = socket.socket()
s.connect(("192.168.178.64", 80))

while True:
  try:
    data = s.recv(100)
    print("SOCKET MSG: "+str(data, 'utf8'), end='')
    #analogVal = analogPin.read()
    #rel_val = analogVal/MAX_ANALOG_VAL
    #print("Analog: "+str(analogVal)+" - rel: "+str(rel_val))
    position = data.split[0]
    color_string = data.split[1]

    print("New Position: "+str(position))
    servo.rotate(position)
    
    colors = stringToInt(color_string)
    print("New Color: "+str(colors))
    ring_led.colorAll(colors[0], colors[1], colors[2])
    sleep_ms(10)
  except socket.error:
    s.close()
    print("Caught socket error")
    continue 