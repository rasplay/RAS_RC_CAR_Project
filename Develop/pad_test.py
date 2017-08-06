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

    while True:
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

                                global speed 
                                speed = 100                        
                                while True:
                                     if action[4] == '01' and action[6] == '01' and action[7] == '01': # Button 
                                         speed -= 25
                                     print speed    
                                     if speed == 0 and speed == 100: 
                                         speed = 100
#                                         print speed
                                

#                        elif action[4] == '01' and action[6] == '01' and action[7] == '01': # Button
#                                pwm2.ChangeDutyCycle(50)
#                                (speed,up) = (0,0)
#                                speed += 25
#                                if speed >= 0 and speed <= 100:
#                                    print speed 
#                                elif speed > 100:
#                                    speed = 0
#                                    print speed
#                                up += speed
#                                else:
#                                        Stop()
       
                            

                        action = []

if __name__ == "__main__":
    main()
