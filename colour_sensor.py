from machine import Pin, ADC
from time import sleep
import math

ldr = ADC(Pin(35))
ldr.atten(ADC.ATTN_11DB)

ledRed = Pin(12, Pin.OUT)
ledGreen = Pin(13, Pin.OUT)
ledBlue = Pin(14, Pin.OUT)

ledArray = [ledRed, ledGreen, ledBlue]
colourArray = [0,0,0]
#whiteArray = [0,0,0]
whiteArray = [2141, 3246, 2536]
#blackArray = [0,0,0]
blackArray = [654, 1622, 1239]

balanceSet = False
avgRead = 0.0

def checkBalance():
  if balanceSet == False:
    setBalance()
  

def setBalance():
  print("setBalance - white")
  sleep(5)
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(0.5)
    getReading(5) 
    global whiteArray
    whiteArray[i] = avgRead
    ledArray[i].value(0)
    sleep(0.5)
  
  print("setBalance - black")
  sleep(5)
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(0.5)
    getReading(5)
    global blackArray
    blackArray[i] = avgRead
    ledArray[i].value(0)
    sleep(0.5)
  
  
  global balanceSet
  balanceSet = True

def checkColour():
  print("checkColour")
  sleep(5)
  for i in range(0,3):
    ledArray[i].value(1)
    sleep(0.1)
    getReading(10)  
    global colourArray
    colourArray[i] = avgRead      
    greyDiff = whiteArray[i] - blackArray[i]  
    print("greyDiff:")
    print(greyDiff)
    #the reading returned minus the lowest value divided by the possible range multiplied by 255
    #will give us a value roughly between 0-255 representing the value for the current reflectivity
    #(for the colour it is exposed to) of what is being scanned
    colourArray[i] = (colourArray[i] - blackArray[i])/(greyDiff)*255 
    ledArray[i].value(0)
    #sleep(0.5)
  
def getReading(times):
  print("getReading")
  tally = 0
  for i in range(0,times):
    reading = ldr.read()
    tally = reading + tally
    sleep(0.05)
  
  global avgRead
  avgRead = (tally)/times
  print(avgRead)


def printColour():
  print("R = ")
  print(max(min(int(colourArray[0]), 255), 0))
  print("G = ")
  print(max(min(int(colourArray[1]), 255), 0))
  print("B = ")
  print(max(min(int(colourArray[2]), 255), 0))
  print("whiteArray:")
  print(whiteArray)
  print("blackArray:")
  print(blackArray)
  sleep(2)

while True:
  #checkBalance()
  checkColour()
  printColour()

