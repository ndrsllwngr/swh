from machine import Pin, ADC
from time import sleep
import math


class DIY_COLOUR_SENSOR():

    SCAN_READINGS = 20
    CALIBRATION_READINGS = 200

    def __init__(self, ldrPin=35, ledRedPin=12, ledGreenPin=13, ledBluePin=14):
        self.ldr = ADC(Pin(ldrPin))
        self.ldr.atten(ADC.ATTN_11DB)

        self.ledRed = Pin(ledRedPin, Pin.OUT)
        self.ledGreen = Pin(ledGreenPin, Pin.OUT)
        self.ledBlue = Pin(ledBluePin, Pin.OUT)

        self.ledArray = [self.ledRed, self.ledGreen, self.ledBlue]
        self.colourArray = [0, 0, 0]
        # [2118.45, 3278.75, 2240.7] #[1839.6, 3192.4, 2062.6] #[2141, 3246, 2536]
        self.whiteArray = [2094.65, 3256.78, 2206.68]
        # [703.7, 1690.4, 980.8] #[693.2, 1698.2, 1000.4] #[654, 1622, 1239]
        self.blackArray = [1152.215, 2087.58, 1359.715]

        self.balanceSet = False

    def checkBalance(self):
        if self.balanceSet == False:
            print("CALIBRATING COLORSENSOR")
            self.setBalance()
            print("White: "+str(self.whiteArray) +
                  " - Black: "+str(self.blackArray))

    def setBalance(self):
        print("setBalance > white")
        sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.5)
            avgRead = self.getReading(self.CALIBRATION_READINGS)
            self.whiteArray[i] = avgRead
            self.ledArray[i].value(0)
            sleep(0.5)

        print("setBalance > black")
        sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.5)
            avgRead = self.getReading(self.CALIBRATION_READINGS)
            self.blackArray[i] = avgRead
            self.ledArray[i].value(0)
            sleep(0.5)

        self.balanceSet = True

    def checkColour(self):
        # print("checkColour")
        # sleep(5)
        for i in range(0, 3):
            self.ledArray[i].value(1)
            sleep(0.1)
            avgRead = self.getReading(self.SCAN_READINGS)
            self.colourArray[i] = avgRead
            greyDiff = self.whiteArray[i] - self.blackArray[i]
            #print("greyDiff: ", greyDiff)
            # the reading returned minus the lowest value divided by the possible range multiplied by 255
            # will give us a value roughly between 0-255 representing the value for the current reflectivity
            # (for the colour it is exposed to) of what is being scanned
            self.colourArray[i] = (
                self.colourArray[i] - self.blackArray[i])/(greyDiff)*255
            self.ledArray[i].value(0)
            # sleep(0.5)
        return self.getColourString()

    def getReading(self, times):
        # print("getReading")
        tally = 0
        for i in range(0, times):
            reading = self.ldr.read()
            tally = reading + tally
            sleep(0.05)
        read = (tally)/times
        # print(read)
        return read

    def printColour(self):
        rVal = max(min(int(self.colourArray[0]), 255), 0)
        gVal = max(min(int(self.colourArray[1]), 255), 0)
        bVal = max(min(int(self.colourArray[2]), 255), 0)
        print("RGB(" + rVal + "," + gVal + "," + bVal + "), whiteArr =", self.whiteArray,
              ", blackArr =", max(min(int(self.colourArray[2]), 255), 0))

    def getColourString(self):
        rVal = max(min(int(self.colourArray[0]), 255), 0)
        gVal = max(min(int(self.colourArray[1]), 255), 0)
        bVal = max(min(int(self.colourArray[2]), 255), 0)
        netColourStr = str(rVal) + "-" + str(gVal) + "-" + str(bVal)
        print("Color Sensor - Scan: " + netColourStr)
        return netColourStr
