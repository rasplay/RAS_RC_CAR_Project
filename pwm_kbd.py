#!/usr/bin/python
# -*- coding: UTF-8 -*-
import curses
import RPi.GPIO as GPIO
from RAS_RC_Motor import *

#set GP

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
               break
            elif char == ord('i'):
                 Toy_Forward()
            elif char == ord('k'):
                 Toy_Backward()
            elif char == ord('l'):
                 Toy_TurnRight()
            elif char == ord('j'):
                 Toy_TurnLeft()
            elif char == ord('s'):
                 Stop()
#            elif char == 10:

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
#except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
