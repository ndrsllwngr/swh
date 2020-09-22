from machine import Pin, I2C
from time import sleep_ms

class MPU6050_GYRO():
    
    # Default I2C address for the MPU6050
    MPU6050_ADDR = 0x68

    # Required MPU6050 registers and their addresses
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38
    GYRO_XOUT_H  = 0x43
    GYRO_YOUT_H  = 0x45
    GYRO_ZOUT_H  = 0x47
    TEMP_OUT_H   = 0X41

    # Calibration defaults
    CALIBRATION_STEPS = 10
    CALIBRARTION_SLEEP = 100

    # Globals
    last_read_time = 0.0   

    last_x_value = 0
    last_y_value = 0
    last_z_value = 0

    # Calibrated measurements to offset some bias or error in the readings.
    calib_x_gyro  = 0.0 
    calib_y_gyro  = 0.0 
    calib_z_gyro  = 0.0 

    def __init__(self, sda_pin=21, scl_pin=22):
        #instantiate the i2c interface on esp32 (pins 21,22 for wroom32 variants) 
        self.i2c = I2C(scl=scl_pin, sda=sda_pin, freq=400000)
        self.init_MPU()
        self.calibrate_sensors()

    def init_MPU(self):
        #write to sample rate register 
        self.i2c.writeto_mem(self.MPU6050_ADDR, self.SMPLRT_DIV, b'\x07')
        #Write to power management register to wake up mpu6050
        self.i2c.writeto_mem(self.MPU6050_ADDR, self.PWR_MGMT_1, b'\x00')
        #Write to Configuration register 
        self.i2c.writeto_mem(self.MPU6050_ADDR, self.CONFIG, b'\x00')
        #Write to Gyro configuration register to self test gyro 
        self.i2c.writeto_mem(self.MPU6050_ADDR, self.GYRO_CONFIG, b'\x18')
        #Set interrupt enable register to 0 .. disable interrupts
        self.i2c.writeto_mem(self.MPU6050_ADDR, self.INT_ENABLE, b'\x00')

    def read_raw_data(self, addr):
        #Gyro value are 16-bit
        high = self.i2c.readfrom_mem(self.MPU6050_ADDR, addr, 1)
        low  = self.i2c.readfrom_mem(self.MPU6050_ADDR, addr+1, 1)
        
        #concatenate higher and lower values
        val = high[0] << 8 | low[0]
            
        #we're expecting a 16 bit signed int (between -32768 to 32768). This step ensures 16 bit unsigned int raw readings are resolved. 
        if(val > 32768):
            val = val - 65536
        return val

    def calibrate_sensors(self):
        x_gyro  = 0
        y_gyro  = 0
        z_gyro  = 0
        
        print("Starting Calibration")

        #Discard the first set of values read from the IMU
        self.read_raw_values()

        # Read and average the raw values from the IMU
        for i in range(self.CALIBRATION_STEPS): 
            values = self.read_raw_values()
            x_gyro  += values[0]
            y_gyro  += values[1]
            z_gyro  += values[2]
            sleep_ms(self.CALIBRARTION_SLEEP)
        
        x_gyro /= self.CALIBRATION_STEPS
        y_gyro /= self.CALIBRATION_STEPS
        z_gyro /= self.CALIBRATION_STEPS

        # Store the raw calibration values globally
        self.calib_x_gyro  = x_gyro
        self.calib_y_gyro  = y_gyro
        self.calib_z_gyro  = z_gyro

        print("Finishing Calibration")
        
    def set_last_read_values(self, x, y, z):
        self.last_x_value = x
        self.last_y_value = y 
        self.last_z_value = z 

    def read_raw_values(self):
        #Read Gyroscope raw value
        gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
        gyro_y = self.read_raw_data(self.GYRO_YOUT_H)
        gyro_z = self.read_raw_data(self.GYRO_ZOUT_H)
        return (gyro_x, gyro_y, gyro_z)    
        
    def read_values(self):
        #Read Gyroscope raw value
        gyro_x, gyro_y, gyro_z = self.read_raw_values()

        # This is angular velocity in each of the 3 directions 
        Gx = (gyro_x - self.calib_x_gyro)/131.0
        Gy = (gyro_y - self.calib_y_gyro)/131.0
        Gz = (gyro_z - self.calib_z_gyro)/131
        return (Gx, Gy, Gz)

    def get_last_time(self): 
        return self.last_read_time

    def get_last_values(self):
        return (self.last_x_value, self.last_y_value, self.last_z_value)