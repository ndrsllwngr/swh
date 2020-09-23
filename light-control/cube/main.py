import os
import utime
import _thread

from drivers.mpu6050 import MPU6050_GYRO
from drivers.colour_sensor import DIY_COLOUR_SENSOR
from drivers.switch import SWITCH
from drivers.speaker import SPEAKER
from time import sleep_ms
from util.netvars import initNet, setNetVar, getNetVar

ip = initNet("Wu-Tang-Lan", "doppelhure69")
print("my ip is: "+ip)
setNetVar("cubeIP", str(ip))

gyro = MPU6050_GYRO()
switch = SWITCH(26)
colour_sensor = DIY_COLOUR_SENSOR()
speaker = SPEAKER()

lastUpdated = utime.time()

import socket
socket_addr = socket.getaddrinfo('0.0.0.0', 9420)[0][-1]

s = socket.socket()
s.bind(socket_addr)
s.listen(1)
print('Listening for new lamps on: ', socket_addr)

color_string = "255-255-255"
gyro_pos = 0.0

clients = []

def listen_for_connections():
    global clients
    while True:
        try:
            cl, addr = s.accept()
            print('New lamp connected: ', addr)
            clients.append((cl,addr))
        except OSError:
            print("Socket closed - stopping to accept connections")
            break

_thread.start_new_thread(listen_for_connections, () )

def send_message_to_connected_clients(msg):
    global clients
    for c in clients:
        client, address = c
        print ("Sending '"+msg+"'to: ",address)
        try:
            client.send(msg+"\n")
        except OSError:
            print(str(address) + " disconnected - OSError")
            client.close()
            clients.remove((client, address))
        except Exception as e:
            print(str(address) + " disconnected - Exception: "+str(e))
            client.close()
            clients.remove((client, address))

def get_message():
    return color_string+"$"+str(gyro_pos)

while True:
    try:
        timeDiff = utime.time() - lastUpdated
        if timeDiff > 30:
            lastUpdated = utime.time()
            cube_reset = getNetVar("cubeReset")
            if cube_reset == 'True':
                print("Got CUBE_RESET")
                print("Resetting cube...")
                setNetVar("cubeReset", False)
                import machine
                machine.reset()

            lamp_reset = getNetVar("lampReset")
            if lamp_reset == 'True':
                print("Got LAMP_RESET")
                print("Resetting all lamps...")
                setNetVar("lampReset", False)
                send_message_to_connected_clients("RESET")

        if len(clients) > 0:        
            if not switch.getValue():
                print("COLOR_SCAN_MODE")
                sleep_ms(1000)
                speaker.beep_long(tone='c')
                sleep_ms(2000)
                speaker.beep_long(tone='d')
                speaker.beep_long(tone='d')
                print("STARTING_SCAN")
                color_string = colour_sensor.checkColour()
                speaker.beep_melody("cc")
                speaker.beep_long('g')

                print("Color scanned: sending: "+get_message())
                send_message_to_connected_clients(get_message())
            else:
                print("GYRO_MODE")
                gyro_pos = gyro.update_position()
                print("Gyro  scanned: sending: "+get_message())
                send_message_to_connected_clients(get_message())
                sleep_ms(100)

        else: 
            print("No connected lamps, waiting for connection")
            sleep_ms(5000)
    except KeyboardInterrupt:
        break
    except OSError as e:
        print("Netvar error: %s" % e)
        continue

print("Exiting...")
print("Closing all clients...")
send_message_to_connected_clients("EOF\n")
print("Closing socket...")
s.close()
