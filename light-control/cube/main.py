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
setNetVar("cupeIP", str(ip))

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
print('listening for new clients on', socket_addr)

color_string = "255-255-255"
gyro_pos = 0.0

clients = []

def listen_for_connections():
    global clients
    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        clients.append((cl,addr))

_thread.start_new_thread(listen_for_connections, () )

def send_message_to_connected_clients(msg):
    global clients
    for c in clients:
        client, address = c
        print ("sending '"+msg+"'to: ",address)
        try:
            client.send(msg)
        except OSError:
            print(address + " disconnected")
            client.close()
            clients.remove((client, address))

while True:
    try:
        timeDiff = utime.time() - lastUpdated
        if timeDiff > 30:
            lastUpdated = utime.time()
            cube_reset = getNetVar("cubeReset")
            if cube_reset == 'True':
                setNetVar("cubeReset", False)
                import machine
                machine.reset()

            lamp_reset = getNetVar("lampReset")
            if lamp_reset == 'True':
                setNetVar("lampReset", False)
                send_message_to_connected_clients("RESET\n")

        if len(clients) > 0:        
            if not switch.getValue():
                speaker.beep_n(2)
                print("COLOR_SCAN_MODE")
                color_string = colour_sensor.checkColour()
                speaker.beep_long(tone='d')
                sleep_ms(500)
            else:
                gyro_pos = gyro.update_position()
                sleep_ms(100)
            message = color_string+"$"+str(gyro_pos)+"\n"
            print("About to send: "+message)

            send_message_to_connected_clients(message)
        else: 
            print("No clients, waiting for connection")
            sleep_ms(1000)
    except KeyboardInterrupt:
        break
    except OSError as e:
        print("Netvar error: %s" % e)
        continue

s.close()
