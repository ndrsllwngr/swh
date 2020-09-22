import neopixel
from machine import Pin
from time import sleep
import random

class RING_LED():

  # number of leds
  LED_COUNT=8
  # connected Pin
  p=0

  def __init__(self, pin = 0):
    self.np = neopixel.NeoPixel(Pin(pin),self.LED_COUNT)

  # colors the led at position in (r,g,b)
  def color(self,position, r,g,b):
    self.np[position]=(r,g,b)
    self.np.write()

  # remove all colors
  def clearAll(self):
    for i in range(self.LED_COUNT):
      self.color(i,0,0,0)

  # remove color from led at position
  def clear(self, position):
    self.color(position,0,0,0)

  def colorAll(self,r,g,b):
    for i in range(self.LED_COUNT):
      # color the current led
      self.color(i,r,g,b)
        
  # the color (r,g,b) should run x times like a cycle 
  def cycleColors(self, wait, x): 
    # before setting new colors, clear the ring
    self.clearAll()
    # the cycle should run x times
    for j in range(x):
      for i in range(self.LED_COUNT):
        if(i==0):
          self.clear(self.LED_COUNT-1)
        else:
          self.clear(i-1)

        r=random.randint(150, 255)
        g=random.randint(0, 100)
        b=random.randint(50, 200)
        # color the current led
        self.color(i,r,g,b)
        
        # wait, color is displayed this time
        sleep(wait)


  # the color (r,g,b) should run x times like a cycle 
  def cycle(self, r,g,b,wait,x): 
    # before setting new colors, clear the ring
    self.clearAll()
    # the cycle should run x times
    for j in range(x):
      for i in range(self.LED_COUNT):
        # clear the previous led
        if(i==0):
          self.clear(self.LED_COUNT-1)
        else:
          self.clear(i-1)
        
        # color the current led
        self.color(i,r,g,b)
        
        # wait, color is displayed this time
        sleep(wait)


