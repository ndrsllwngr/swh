#import module
from netvars import setNetVar, getNetVar, initNet

# # assuming there is a network with ssid hotspot1 and password 123456789
# connect to wifi
initNet("wifi", "pwd")

# set the variale with the name test222 to the value valTest222
setNetVar("test222", "valTest222")

# read the variable test222 from the server and print it
a = getNetVar("test222")
print(a)  # will print valTest222
