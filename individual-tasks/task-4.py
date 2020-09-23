from machine import I2C, Pin, ADC
import ssd1306
from time import sleep

light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)

MAX_ANALOG_VAL = 4095

i2c = I2C(-1, scl=Pin(15), sda=Pin(4))

# display size
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
    light_value = light_sensor.read()
    print(light_value)
    rel_val = light_value/MAX_ANALOG_VAL
    brightness_string = "Light: " + str(100-rel_val*100)+"%"
    oled.fill(0)
    oled.show()
    oled.text('Light Sensor', 0, 0)
    oled.text(brightness_string, 0, 10)
    oled.show()
    sleep(1)
