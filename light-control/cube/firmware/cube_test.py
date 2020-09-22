from drivers.mpu6050 import MPU6050_GYRO
from drivers.colour_sensor import DIY_COLOUR_SENSOR
from drivers.switch import SWITCH
from drivers.speaker import SPEAKER
from time import sleep_ms 
from util.netvars import initNet, setNetVar

initNet("Wu-Tang-Lan", "doppelhure69")

gyro = MPU6050_GYRO()
switch = SWITCH(26)
colour_sensor = DIY_COLOUR_SENSOR()
speaker = SPEAKER()

while True:
    try:
        gyro_pos = gyro.update_position()
        setNetVar("lampPosition", gyro_pos)
        if not switch.getValue():
            speaker.beep_n(2)
            print("COLOR_SCAN_MODE")
            color_string = colour_sensor.checkColour()
            setNetVar("lampColour", color_string)
            speaker.beep_long(tone='d')
            sleep_ms(500)
        sleep_ms(20)
    except KeyboardInterrupt:
        break