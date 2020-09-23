import os
import utime

from drivers.mpu6050 import MPU6050_GYRO
from drivers.colour_sensor import DIY_COLOUR_SENSOR
from drivers.switch import SWITCH
from drivers.speaker import SPEAKER
from time import sleep_ms
from util.netvars import initNet, setNetVar, getNetVar

ip = initNet("Wu-Tang-Lan", "doppelhure69")
print("my ip is: "+ip)
setNetVar("cupeIP", str(ip))

gyro = MPU6050_GYRO()
switch = SWITCH(26)
colour_sensor = DIY_COLOUR_SENSOR()
speaker = SPEAKER()

lastUpdated = utime.time()

import socket
addr = socket.getaddrinfo('0.0.0.0', 9420)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

color_string = "255-255-255"
gyro_pos = 0.0

while True:
    print('listening for new clients on', addr)
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        while True:
            timeDiff = utime.time() - lastUpdated
            if timeDiff > 30:
                lastUpdated = utime.time()
                reset = getNetVar("cubeReset")
                if reset == 'True':
                    setNetVar("cubeReset", False)
                    import machine
                    machine.reset()
            if not switch.getValue():
                speaker.beep_n(2)
                print("COLOR_SCAN_MODE")
                color_string = colour_sensor.checkColour()
                speaker.beep_long(tone='d')
                sleep_ms(500)
            else:
                gyro_pos = gyro.update_position()
                sleep_ms(30)
            message = color_string+"$"+str(gyro_pos)
            print("About to send: "+message)
            cl.send(message)
    except KeyboardInterrupt:
        break
    except OSError as e:
        print("Socket error: %s" % e)
        cl.close()

s.close()
