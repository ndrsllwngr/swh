import neopixel
from machine import Pin
from time import sleep
import random

# number of leds
n=8
# connected Pin
p=0

np = neopixel.NeoPixel(Pin(p),n)

# colors the led at position in (r,g,b)
def color(position, r,g,b):
  np[position]=(r,g,b)
  np.write()

# remove all colors
def clearAll():
  for i in range(n):
    color(i,0,0,0)

# remove color from led at position
def clear(position):
  color(position,0,0,0)

def colorAll(r,g,b):
  for i in range(n):
    # color the current led
    color(i,r,g,b)
      
# the color (r,g,b) should run x times like a cycle 
def cycleColors(wait,x): 
  # before setting new colors, clear the ring
  clearAll()
  print("cycling")
  # the cycle should run x times
  for j in range(x):
    for i in range(n):
      if(i==0):
        clear(n-1)
      else:
        clear(i-1)

      r=random.randint(150, 255)
      g=random.randint(0, 100)
      b=random.randint(50, 200)
      # color the current led
      color(i,r,g,b)
      
      # wait, color is displayed this time
      sleep(wait)


# the color (r,g,b) should run x times like a cycle 
def cycle(r,g,b,wait,x): 
  # before setting new colors, clear the ring
  clearAll()
  print("cycling")
  # the cycle should run x times
  for j in range(x):
    for i in range(n):
      # clear the previous led
      if(i==0):
        clear(n-1)
      else:
        clear(i-1)
      
      # color the current led
      color(i,r,g,b)
      
      # wait, color is displayed this time
      sleep(wait)


