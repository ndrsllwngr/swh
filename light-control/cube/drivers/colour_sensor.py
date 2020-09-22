from machine import Pin, ADC
from time import sleep
import math


class DIY_COLOUR_SENSOR():

    def __init__(self, ldrPin=35, ledRedPin=12, ledGreenPin=13, ledBluePin=14):
        self.ldr = ADC(Pin(ldrPin))
        self.ldr.atten(ADC.ATTN_11DB)

        self.ledRed = Pin(ledRedPin, Pin.OUT)
        self.ledGreen = Pin(ledGreenPin, Pin.OUT)
        self.ledBlue = Pin(ledBluePin, Pin.OUT)

        self.ledArray = [self.ledRed, self.ledGreen, self.ledBlue]
        self.colourArray = [0, 0, 0]
        self.whiteArray = [2141, 3246, 2536]  # [0,0,0]
        self.blackArray = [654, 1622, 1239]  # [0,0,0]

        self.balanceSet = False
        self.avgRead = 0.0

    def checkBalance(self):
        if self.balanceSet == False:
            self.setBalance()

    def setBalance(self):
        print("setBalance > white")
        sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.5)
            self.getReading(5)
            self.whiteArray[i] = self.avgRead
            self.ledArray[i].value(0)
            sleep(0.5)

        print("setBalance > black")
        sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.5)
            self.getReading(5)
            self.blackArray[i] = self.avgRead
            self.ledArray[i].value(0)
            sleep(0.5)

        self.balanceSet = True

    def checkColour(self):
        print("checkColour")
        sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.1)
            self.getReading(10)
            self.colourArray[i] = self.avgRead
            greyDiff = self.whiteArray[i] - self.blackArray[i]
            print("greyDiff: ", greyDiff)
            # the reading returned minus the lowest value divided by the possible range multiplied by 255
            # will give us a value roughly between 0-255 representing the value for the current reflectivity
            # (for the colour it is exposed to) of what is being scanned
            self.colourArray[i] = (
                self.colourArray[i] - self.blackArray[i])/(greyDiff)*255
            self.ledArray[i].value(0)
            # sleep(0.5)

    def getReading(self, times):
        print("getReading")
        tally = 0
        for i in range(0, times):
            reading = self.ldr.read()
            tally = reading + tally
            sleep(0.05)

        self.avgRead = (tally)/times
        print(self.avgRead)

    def printColour(self):
        rVal = max(min(int(self.colourArray[0]), 255), 0)
        gVal = max(min(int(self.colourArray[1]), 255), 0)
        bVal = max(min(int(self.colourArray[2]), 255), 0)
        print("RGB(", rVal, ",", gVal, ",", bVal, "), whiteArr = ", self.whiteArray,
              ", blackArr = ", max(min(int(self.colourArray[2]), 255), 0))
        sleep(2)

    def run(self):
        while True:
            # self.checkBalance()
            self.checkColour()
            self.printColour()
