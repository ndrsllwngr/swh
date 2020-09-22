import network
from time import sleep

def initNet(ssid, passwd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, passwd)
        while not wlan.isconnected():

            pass
    print('network config:', wlan.ifconfig())

def http_get(url):
    #print(url)
    #print("............")
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    retStr =""
    while True:
        data = s.recv(500)
        if data:
            retStr = str(data, 'utf8') 
        else:
            break
    s.close()
    return retStr


def setNetVar(varName, varVal):
    urlStr = "https://ubicomp.net/sw/db1/var2db.php?varName=" + str(varName) + "&varValue=" + str(varVal)
    http_get(urlStr)


def getNetVar(varName):
    urlStr = "https://ubicomp.net/sw/db1/var2db.php?varName=" + str(varName) 
    resStr = http_get(urlStr)
    import ure
    reg1 = ure.compile('\r\n\r\n|\n\n')
    reg2 = ure.compile(' |\n|\r')
    _, retVar0 = reg1.split(resStr)
    retVar = reg2.split(retVar0)
    return retVar[0]