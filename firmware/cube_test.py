from drivers.mpu6050 import MPU6050_GYRO
from time import sleep_ms 

def read_gyro(gyro):
    try:
        while True:
            
            gyro_x, gyro_y, gyro_z = gyro.read_values()

            gyro.set_last_read_values(gyro_x,gyro_y,gyro_z)

            sensitivity = 3

            dir = "NONE "

            if gyro_z > sensitivity:
                dir = "RIGHT"
            elif gyro_z < -sensitivity:
                dir = "LEFT "

            print(dir+" - %.2f," %gyro_z)

            sleep_ms(100)

    except KeyboardInterrupt:
        pass


gyro = MPU6050_GYRO()
read_gyro(gyro)