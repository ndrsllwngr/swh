from time import sleep
from machine import PWM, Pin

# Values for 500hz servo

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
        print("INIT")
        self.servo.duty(self.DUTY_MAX)

    # position needs to be between 0.0 and 1.0
    def rotate(self, pos):
        position = self.MAX_POS - pos * (self.MAX_POS - self.MIN_POS)
        print("desired position: "+ str(position))
        
        current_duty = self.servo.duty()

        if(current_duty>self.DUTY_MAX):
            current_duty = self.DUTY_MAX

        print("curr duty: " + str(current_duty))

        new_duty = int(self.DUTY_MIN + position * (self.DUTY_MAX - self.DUTY_MIN))
        
        # If new_duty is out of bounds correct it
        if(new_duty > self.DUTY_MAX):
            new_duty = self.DUTY_MAX
        elif new_duty < self.DUTY_MIN:
            new_duty = self.DUTY_MIN

        print("new duty: " + str(new_duty))

        step = 1 if current_duty < new_duty else -1

        for i in range(current_duty, new_duty+1, step):
            self.servo.duty(i)
            sleep(self.SLEEP)