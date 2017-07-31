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

                        num = int(action[5], 16) # Translate back to integer form
                        percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] # Calculate the percentage of push
                        percent128 = str((float(num)/127.0))[2:4]

                        print '%s' % action

                        if percent254 == '.0':
                                percent254 = '100'
                        if percent128 == '0':
                                percent128 = '100'

                        if action[6] == '01' : # Button
                                if action[4] == '01' or '09':
                                        print 'You pressed button: ' + action[7]
                                else:
                                        print 'You released button: ' + action[7]

                        elif action[7] == '08': # D-pad left/right
                                if action[4] == 'FF':
                                        print 'You pressed right on the D-pad'
                                        TurnRight()
                                elif action[4] == '01':
                                        print 'You pressed left on the D-pad'
                                        TurnLeft()
                                else:
                                        print 'You released the D-pad'
                                        Stop()


                        elif action[7] == '09': # D-pad up/down
                                if action[4] == 'FF':
                                        print 'You pressed down on the D-pad'
                                        Backward()
                                elif action[4] == '01':
                                        print  'You pressed up on the D-pad'
                                        Forward()
                                else:
                                        print 'You released the D-pad'
                                        Stop()

                        elif action[7] == '01': # Left Joystick up/down
                                if action[4] == 'FF':
                                        print 'You pressed down on the left joystick'
                                        Backward()
                                elif action[4] == '01':
                                        print 'You pressed up on the left joystick'
                                        Forward()
                                else:
                                        print 'You released the left joystick'
                                        Stop()

                        elif action[7] == '02': # Right Joystick left/right
                                num = int(action[5], 16) # Translate back into integer form
                                if num >= 128:
                                        print 'You moved the right joystick left to %' + percent254
                                        TurnLeft()
                                elif num <= 127 \
                                and num != 0:
                                        print 'You moved the right joystick right to %' + percent128
                                        TurnRight()
                                else:
                                        print 'You Stopped moving the right joystick'
                                        Stop()

                        action = []

if __name__ == "__main__":
    main()


