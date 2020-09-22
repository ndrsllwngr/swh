from machine import Pin
from time import sleep

class VibMotor():

	def __init__(self, pin = 5):
		self.motor = Pin(pin, Pin.OUT)

	def start_vibration(self):
		while True:
			self.motor.value(1)
			sleep(0.4)
			self.motor.value(0)
			sleep(1)