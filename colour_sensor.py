from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(35))
ldr.atten(ADC.ATTN_11DB)

ledGreen = Pin(12, Pin.OUT)
ledRed = Pin(13, Pin.OUT)
ledBlue = Pin(14, Pin.OUT)

ledArray = [ledGreen,ledRed,ledBlue]
colourArray = [0,0,0]
whiteArray = [0,0,0]
blackArray = [0,0,0]

balanceSet = False
avgRead = 0.0

#green = 0
#red = 0
#blue = 0

def checkBalance():
  if balanceSet == False:
    setBalance()
  

def setBalance():
  sleep(1)
  print("setBalance - white")
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(1)
    getReading(5) 
    global whiteArray
    whiteArray[i] = avgRead
    ledArray[i].value(0)
    sleep(1)
  
  sleep(5)             

  print("setBalance - black")
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(1)
    getReading(5)
    global blackArray
    blackArray[i] = avgRead
    #blackArray[i] = analogRead(2)
    ledArray[i].value(0)
    sleep(1)
  
  
  global balanceSet
  balanceSet = True

  sleep(5)

  
def checkColour():
  print("checkColour")
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(1)                    
    getReading(5)  
    global colourArray
    colourArray[i] = avgRead      
    greyDiff = whiteArray[i] - blackArray[i]  
    print("greyDiff:")
    print(greyDiff)
    colourArray[i] = (colourArray[i] - blackArray[i])/(greyDiff)*255 #the reading returned minus the lowest value divided by the possible range multiplied by 255 will give us a value roughly between 0-255 representing the value for the current reflectivity(for the colour it is exposed to) of what is being scanned
    ledArray[i].value(0)
    sleep(1)
  
def getReading(times):
  print("getReading")
  tally = 0
  for i in range(0,times):
    reading = ldr.read()
    tally = reading + tally
    sleep(1)
  
  global avgRead
  avgRead = (tally)/times
  print(avgRead)


def printColour():
  print("R = ")
  print(int(colourArray[1]))
  print("G = ")
  print(int(colourArray[0]))
  print("B = ")
  print(int(colourArray[2]))
  sleep(2)

while True:
  checkBalance()
  checkColour()
  printColour()

