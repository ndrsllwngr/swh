# fusiontest.py Simple test program for sensor fusion on Pyboard
# Author Peter Hinch
# Released under the MIT License (MIT)
# Copyright (c) 2017 Peter Hinch
# V0.8 14th May 2017 Option for external switch for cal test. Make platform independent.
# V0.7 25th June 2015 Adapted for new MPU9x50 interface

from machine import Pin
#import pyb
import utime as time
from drivers.imu import MPU6050
from drivers.mpu9250 import MPU9250
from fusion.fusion import Fusion

imu = MPU9250('X')

fuse = Fusion()

runs = 0

# Code for external switch
# switch = Pin('Y7', Pin.IN, pull=Pin.PULL_UP) # Switch to ground on Y7
# TODO implement switch


def sw():
    global runs
    if runs > 50:
        return True
    else:
        runs += 1
        return False  # TODOnot switch.value()
# Code for Pyboard switch
#sw = pyb.Switch()


# Choose test to run
Calibrate = True
Timing = True


def getmag():                               # Return (x, y, z) tuple (blocking read)
    return imu.mag.xyz


if Calibrate:
    print("Calibrating. Press switch when done.")
    fuse.calibrate(getmag, sw, 100)
    print(fuse.magbias)

if Timing:
    mag = imu.mag.xyz  # Don't include blocking read in time
    accel = imu.accel.xyz  # or i2c
    gyro = imu.gyro.xyz
    start = time.ticks_us()  # Measure computation time only
    fuse.update(accel, gyro, mag)  # 1.97mS on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (uS):", t)

count = 0
while True:
    # Note blocking mag read
    fuse.update(imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
    if count % 50 == 0:
        print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(
            fuse.heading, fuse.pitch, fuse.roll))
    time.sleep_ms(20)
    count += 1
