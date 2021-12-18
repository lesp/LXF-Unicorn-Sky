import skywriter
import signal
import unicornhat as unicorn
import time
import random

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

@skywriter.tap()
def tap(position):
    for i in range(1000):
        x = random.randint(0,8)
        y = random.randint(0,8)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        unicorn.set_pixel(x,y,r,g,b)
        unicorn.show()
        time.sleep(0.01)

@skywriter.flick()
def flick(start,finish):
    if start == "south" and finish == "north":
        print("Red")
        for y in range(height):
            for x in range(width):
                unicorn.set_pixel(x,y,255,0,0)
            unicorn.show()
            time.sleep(0.05)
    elif start == "north" and finish == "south":
        print("Green")
        for y in range(height):
            for x in range(width):
                unicorn.set_pixel(x,y,0,255,0)
            unicorn.show()
            time.sleep(0.05)
    elif start == "east" and finish == "west":
        print("Blue")
        for y in range(height):
            for x in range(width):
                unicorn.set_pixel(x,y,0,0,255)
            unicorn.show()
            time.sleep(0.05)
    elif start == "west" and finish == "east":
        print("OFF")
        for y in range(height):
            for x in range(width):
              unicorn.set_pixel(x,y,0,0,0)
              unicorn.show()

signal.pause()
