from drivers.servo import LAMP_SERVO
import utime
import socket
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar, setNetVar
from util.colour import stringToInt

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")
lastColorStr = "0-0-0"
lastUpdated = utime.time()
init = False

cube_ip = getNetVar("cupeIP")

s = socket.socket()
s.connect((cube_ip, 9420))

while True:
    try:
        timeDiff = utime.time() - lastUpdated
        if timeDiff > 30:
            lastUpdated = utime.time()
            reset = getNetVar("lampReset")
            if reset == 'True':
                setNetVar("lampReset", False)
                import machine
                machine.reset()
    
        socket_data = s.recv(100)
        print("Received from socket: "+socket_data)
        colors = stringToInt(socket_data.split("$")[0])
        position = socket_data.split("$")[1]

        servo.rotate(position)
        colorStr = str(colors)

        print("Pos: "+str(position)+" Color: "+colorStr+" TimeDiff: "+str(timeDiff))
        if init == False:
            print("SET COLOR!")
            ring_led.colorAll(colors[0], colors[1], colors[2])
            init = True
        if colorStr != lastColorStr:
            ring_led.colorAll(colors[0], colors[1], colors[2])
            print("New Color: "+colorStr)
            lastColorStr = colorStr
        sleep_ms(30)
    except OSError :
        print("Caught an OSError trying to reconnect socket")
        s.close()
        s = socket.socket()
        s.connect((cube_ip, 9420))
        continue
    except KeyboardInterrupt:
        s.close()

        break

s.close()
