from drivers.mpu6050 import MPU6050_GYRO
from drivers.colour_sensor import DIY_COLOUR_SENSOR
from drivers.switch import SWITCH
from drivers.speaker import SPEAKER
from time import sleep_ms
from util.netvars import initNet, setNetVar
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]


initNet("Wu-Tang-Lan", "doppelhure69")

gyro = MPU6050_GYRO()
switch = SWITCH(26)
colour_sensor = DIY_COLOUR_SENSOR()
speaker = SPEAKER()

s = socket.socket()
s.bind(addr)
s.listen(1)

current_color = "255-255-255"
current_gyro_pos = 0.0

print('listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        
        cl.send(current_color+"%"+str(current_gyro_pos))
        while True:
            current_gyro_pos = gyro.update_position()
            if not switch.getValue():
                speaker.beep_n(2)
                print("COLOR_SCAN_MODE")
                current_color = colour_sensor.checkColour()
                speaker.beep_long(tone='d')
                sleep_ms(500)
                cl.send(current_color+"%"+str(current_gyro_pos))
            sleep_ms(20)
    except socket.error:
        cl.close()
        print("Caught socket error")
        continue 
    except KeyboardInterrupt:
        break
