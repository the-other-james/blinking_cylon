#!/usr/bin/env python

# Display "Cylon" style bouncing red light

import colorsys
import time
import numpy as np

import blinkt

from sys import exit


blinkt.set_clear_on_exit()

position = 0.0
speed_scale = 7
time_step = 0.05
thickness = 0.06

direction = 1
t = 0.01
while True:
    start = time.time()
    
    position = position + (direction * (speed_scale * t))
    if position > 1:
        direction = -1
    elif position < 0:
        direction = 1
    # print("Position: ", position)
        
    for index in range(0, blinkt.NUM_PIXELS):
        # for each LED calculate distance from current position
        location = index / float(blinkt.NUM_PIXELS - 1)
        distance = abs(location - position)
        # print("Location: ", location, " Distance: ", distance)
        # calculate intensity based on distance
        r = np.exp(-np.power(distance, 2.0) / (2 * np.power(thickness, 2.0)))
        r = r * 255
        # print("Set pixel ", index, " to ", r)
        blinkt.set_pixel(index, r, 0, 0)

    blinkt.show()


    end = time.time()
    t = end - start

    if t < time_step:
        time.sleep(time_step - t)
