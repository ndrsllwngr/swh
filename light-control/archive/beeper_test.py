# beeper code from https://micropython-on-esp8266-workshop.readthedocs.io/en/latest/basics.html#beepers
from machine import Pin, PWM
from time import sleep

tempo = 1
# notes and corresponding frequency
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    ' ': 0,
}
pin = Pin(27, Pin.OUT)
# Init Beeper without frequency.
beeper = PWM(pin, duty=512)
melody = 'cdefggaaaagaaaagffffeeddddc'
rhythm = [8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 4, 8,
          8, 8, 8, 4, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 4]

for tone, length in zip(melody, rhythm):
    beeper.freq(tones[tone])
    sleep(tempo/length)

beeper.deinit()
