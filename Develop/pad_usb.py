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

pwm_value = 0

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
                                print ('Speed Change !!! ')
                                print ('befor pwm = '+ str(pwm_value))  
                                pwm_value += 1
                                if pwm_value > 4:
                                    pwm_value = 0
                                print ('current pwm = '+ str(pwm_value))
                                pwm2.ChangeDutyCycle(pwm_value*25)

                        action = []

if __name__ == "__main__":
    main()


