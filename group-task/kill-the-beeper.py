from machine import Pin, PWM

beeper = PWM(Pin(27, Pin.OUT), duty=512)
beeper.deinit()
