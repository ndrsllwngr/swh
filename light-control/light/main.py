from drivers.servo import LAMP_SERVO
import socket
from machine import Pin, PWM, ADC
from time import sleep_ms
from drivers.ring_led import RING_LED
from util.netvars import initNet, getNetVar, setNetVar
from util.colour import stringToInt

servo = LAMP_SERVO()
ring_led = RING_LED()

initNet("Wu-Tang-Lan", "doppelhure69")

cube_ip = getNetVar("cubeIP")


while True:
    try:
        sleep_ms(2000)
        s = socket.socket()
        s.settimeout(10.0)
        s.connect((cube_ip, 9420))
    except OSError:
        print("No cube found, retrying.")
        s.close()
        sleep_ms(1000)
        continue
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

    while True:
        try:
            socket_data = s.readline()
            if not socket_data:
                print("not socket_data")
                s.close()
                break
            socket_data_str = str(socket_data, 'utf8').rstrip()
            print("Received from socket: "+socket_data_str)
            if socket_data_str == "EOF":
                print("EOF")
                s.close()
                break
            if socket_data_str == "RESET":
                print("Reset triggered...")
                import machine
                machine.reset()

            colors_str = socket_data_str.split("$")[0]
            colors = stringToInt(colors_str)
            pos_str = socket_data_str.split("$")[1]
            position = float(pos_str)

            servo.rotate(position)
            colorStr = str(colors)

            print("Pos: "+str(position)+", Color: "+colorStr)
            ring_led.colorAll(colors[0], colors[1], colors[2])
            sleep_ms(30)
        except OSError:
            print("Caught an OSError trying to reconnect socket")
            s.close()
            break
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            s.close()
            break
        except Exception as e:
            print("Expection error: %s" % e)
            continue

print("EXIT")
