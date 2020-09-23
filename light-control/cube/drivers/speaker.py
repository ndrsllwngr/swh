from machine import Pin, PWM
from time import sleep_ms


class SPEAKER():
    SHORT = 200
    LONG = 400

    TONES = {
        'c': 262,
        'd': 294,
        'e': 330,
        'f': 349,
        'g': 392,
        'a': 440,
        'b': 494,
        'C': 523,
        ' ': 0
    }

    def __init__(self, pin=27):
        self.beeper_pin = Pin(pin, Pin.OUT)

    def beep(self, time, tone='c'):
        beeper = PWM(self.beeper_pin, duty=512)
        beeper.freq(self.TONES[tone])
        sleep_ms(time)
        beeper.deinit()

    def beep_short(self, tone='c'):
        self.beep(self.SHORT)
        sleep_ms(int(self.SHORT/4))

    def beep_long(self, tone='c'):
        self.beep(self.LONG)
        sleep_ms(int(self.LONG/4))

    def beep_n(self, n, time=SHORT):
        for i in range(n):
            self.beep(time)
            sleep_ms(int(time/4))
    
    def beep_melody(self, tones, time=SHORT):
        for t in tones:
            self.beep(time)
            sleep_ms(int(time/4))
