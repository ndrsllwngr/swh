from time import sleep
from machine import PWM, Pin


class LAMP_SERVO():

    FREQ = 500
    DUTY_MIN = 120
    DUTY_MAX = 1023
    SLEEP = 0.0005
    MIN_POS = 0.60
    MAX_POS = 1.0

    def __init__(self, pin=26):

        servoPin = Pin(pin, Pin.OUT)

        servo = PWM(servoPin, freq=self.FREQ)
        servo.deinit()
        self.servo = PWM(servoPin, freq=self.FREQ)
        self.servo.duty(self.DUTY_MAX)

    # position needs to be between 0.0 and 1.0
    def rotate(self, pos):
        position = self.MAX_POS - pos * (self.MAX_POS - self.MIN_POS)
        current_duty = self.servo.duty()
        if(current_duty > self.DUTY_MAX):
            current_duty = self.DUTY_MAX

        new_duty = int(self.DUTY_MIN + position *
                       (self.DUTY_MAX - self.DUTY_MIN))

        # If new_duty is out of bounds correct it
        if(new_duty > self.DUTY_MAX):
            new_duty = self.DUTY_MAX
        elif new_duty < self.DUTY_MIN:
            new_duty = self.DUTY_MIN

        print("New duty: " + str(new_duty) + ", Old Duty: " +
              str(current_duty) + ", Desired pos: " + str(position))

        step = 1 if current_duty < new_duty else -1

        self.servo.duty(new_duty)
