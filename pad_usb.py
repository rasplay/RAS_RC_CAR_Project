#!/usr/bin/python
# USB GAMEPAD Joystick RC Car Controller
#
# Created by RaspberryPi Village
#
import sys
import RPi.GPIO as gpio
import time
from motor import *

pipe = None

def main():
    global pipe
    pipe = open('/dev/input/js0','r')

    print 'success'
    readJoystick()

def readJoystick():
    action = []

    while 1:
         for character in pipe.read(1):
                action += ['%02X' % ord(character)]

                if len(action) == 8:

                        print '%s' % action

                        if action[6] == '02' and action[7] == '00': # D-Pad
                                if action[4] == 'FF' and action[5] == '7F':
                                        Toy_TurnRight()
                                elif action[4] == '01' and action[5] == '80':
                                        Toy_TurnLeft()
                                else:
                                         Stop()

                        elif action[6] == '02' and action[7] == '01': # D-Pad
                                if action[4] == 'FF' and action[5] == '7F':
                                        Toy_Backward()
                                elif action[4] == '01' and action[5] == '80':
                                        Toy_Forward()
                                else:
                                         Stop()

                        elif action[6] == '01' and action[7] == '01': # Button
                                        print 'Speed Change !!!'
                                        pwm2.ChangeDutyCycle(a)

                        action = []

if __name__ == "__main__":
    main()


