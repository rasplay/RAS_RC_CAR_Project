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

                        num = int(action[5], 16) # Translate back to integer form
                        percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] # Calculate the percentage of push
                        percent128 = str((float(num)/127.0))[2:4]

                        print '%s' % action

                        if percent254 == '.0':
                                percent254 = '100'
                        if percent128 == '0':
                                percent128 = '100'

#                        if action[6] == '02' : # Button
#                                if action[4] == '01' or '09':
#                                        print 'You pressed button: ' + action[7]
#                                else:
#                                        print 'You released button: ' + action[7]

                        if action[6] == '02' and action[7] == '08': # D-pad left/right
                                if action[4] == 'FF' and action[5] == '7F':
                                        print 'You pressed right on the D-pad'
                                        Toy_TurnRight()
                                elif action[4] == '01' and action[5] == '80':
                                        print 'You pressed left on the D-pad'
                                        Toy_TurnLeft()
                                else:
                                        print 'You released the D-pad'
                                        Stop()

                        elif action[6] == '02' and action[7] == '09': # D-pad up/down
                                if action[4] == 'FF' and action[5] == '7F':
                                        print 'You pressed down on the D-pad'
                                        Toy_Backward()
                                elif action[4] == '01' and action[5] == '80':
                                        print  'You pressed up on the D-pad'
                                        Toy_Forward()
                                else:
                                        print 'You released the D-pad'
                                        Stop()

                        elif action[6] == '02' and action[7] == '01': # Left Joystick up/down
                                if action[4] == 'FF' and action[5] == '7F':
                                        print 'You pressed down on the left joystick'
                                        Toy_Backward()
                                elif action[4] == '01' and action[5] == '80':
                                        print 'You pressed up on the left joystick'
                                        Toy_Forward()
                                else:
                                        print 'You released the left joystick'
                                        Stop()

                        elif action[6] == '02' and action[7] == '02': # Right Joystick left/right
                                if action[4] == 'FF' and action[5] == '7F':
                                        print 'You pressed right on the right joystick'
                                        Toy_TurnRight()
                                elif action[4] == '01' and action[5] == '80':
                                        print 'You pressed left on the right joystick'
                                        Toy_TurnLeft()
                                else:
                                        print 'You released the right joystick'
                                        Stop()

                        elif action[6] == '01' and action[7] == '06': # Button
                                print ('Speed Change !!! ')
                                print ('befor pwm = '+ str(pwm_value))  
                                pwm_value += 1
                                if pwm_value > 4:
                                    pwm_value = 0
                                print ('current pwm = '+ str(pwm_value))
                                pwm2.ChangeDutyCycle(pwm_value*25)


#                                num = int(action[5], 16) # Translate back into integer form
#                                if num >= 128:
#                                        print 'You moved the right joystick left to %' + percent254
#                                        Toy_TurnLeft()
#                                elif num <= 127 \
#                                and num != 0:
#                                        print 'You moved the right joystick right to %' + percent128
#                                        Toy_TurnRight()
#                                else:
#                                        print 'You Stopped moving the right joystick'
#                                        Stop()

                        action = []
 
if __name__ == "__main__":
    main()


