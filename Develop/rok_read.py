import sys
import RPi.GPIO as gpio
import time

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

#                        print int(str(action))
                                        
                        action = []

if __name__ == "__main__":
    main()
