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

                        if action[6] == '01' : # Button
                                if action[4] == '01' or '09':
                                        print 'You pressed button: ' + action[7]
                                else:
                                        print 'You released button: ' + action[7]

                        elif action[7] == '00': # D-pad left/right
                                if action[4] == 'FF':
                                        print 'You pressed right on the D-pad'
                                        TurnRight()
                                elif action[4] == '01':
                                        print 'You pressed left on the D-pad'
                                        TurnLeft()
                                else:
                                        print 'You released the D-pad'
                                        Stop()

                        elif action[7] == '01': # D-pad up/down
                                if action[4] == 'FF':
                                        print 'You pressed down on the D-pad'
                                        Backward()
                                elif action[4] == '01':
                                        print  'You pressed up on the D-pad'
                                        Forward()
                                else:
                                        print 'You released the D-pad'
                                        Stop()

                        action = []

if __name__ == "__main__":
    main()


