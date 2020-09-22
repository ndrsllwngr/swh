from drivers.mpu6050 import MPU6050_GYRO
from time import sleep_ms 
from util.netvars import initNet, setNetVar

DIVIDER = 200

def read_gyro(gyro):

    initNet("Wu-Tang-Lan", "doppelhure69")
    position = 0.0

    try:
        while True:
            
            gyro_x, gyro_y, gyro_z = gyro.read_values()

            gyro.set_last_read_values(gyro_x,gyro_y,gyro_z)

            sensitivity = 3

            dir = "NONE "

            if gyro_z > sensitivity:
                dir = "RIGHT"
                position += gyro / DIVIDER
            elif gyro_z < -sensitivity:
                dir = "LEFT "
                position -= gyro / DIVIDER
            print(dir+" - %.2f," %gyro_z)

            if position > 1.0:
                position = 1.0
            elif position < 0.0:
                position = 0.0

            setNetVar("superCoolLampControllerPosition", position)

            sleep_ms(100)

    except KeyboardInterrupt:
        pass


gyro = MPU6050_GYRO()
read_gyro(gyro)