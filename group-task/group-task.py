import os
from machine import Pin, ADC, PWM, I2C,
from time import sleep
from netvars import setNetVar, getNetVar, initNet
import ssd1306

MAX_ANALOG_VAL = 4095

# init light sensor
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)

# init beeper
beeper = PWM(Pin(27, Pin.OUT), duty=512)
beeper.deinit()
beeper = PWM(Pin(27, Pin.OUT), duty=512)

# init switch
switch = Pin(26, Pin.IN)

# init display
i2c = I2C(-1, scl=Pin(15), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# init wifi
initNet("wifi", "pwd")


while True:

    switch_on = switch.value()

    # when the switch is on read values from light sensor and write them to a netvar
    if switch_on:
        # switch beeper off
        beeper.duty(0)

        # get light sensor value
        light_value = light_sensor.read()

        # convert light_value to a frequency
        sound_value = int(light_value/4)

        oled.fill(0)
        oled.show()
        oled.text('SENSOR MODE', 0, 0)
        oled.text('Frequency: ' + str(sound_value), 0, 10)
        oled.show()

        # save frequency to netvar
        setNetVar("andyandisound", sound_value)

    # when the switch is off read values from a netvar and play them on a speaker
    else:
        # switch beeper on
        beeper.duty(512)

        # get frequency from netvar
        sound_value_web = int(getNetVar("andyandisound"))

        oled.fill(0)
        oled.show()
        oled.text('PLAY MODE', 0, 0)
        oled.text('Frequency: ' + str(sound_value_web), 0, 10)
        oled.show()

        # play sound_value_web (frequency) on speaker
        beeper.freq(int(sound_value_web))

    sleep(0.1)
