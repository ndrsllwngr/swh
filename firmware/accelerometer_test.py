from machine import Pin
from time import sleep
from drivers.imu import MPU6050
from fusion.fusion import Fusion


imu = MPU6050("X")

while True:
    print(str(imu.accel.xyz)+" - "+str(imu.gyro.xyz))
    sleep(0.5)