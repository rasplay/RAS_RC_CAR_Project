import socket
import sys

s = None
pipe = None

def main():
    host = '192.168.0.7'
    port = 10000

    global s
    global pipe

    print 'Try Socket Open'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    pipe = open('/dev/input/js0','r')
    action = []
    spacing = 0

    s.connect((host,port))
    print 'connection End'
    sys.stdout.write('%')

    #joyinit()
    #print 'joyinit() OK'

    data = ' '

    while 1:
         for character in pipe.read(1):
                action += ['%02X' % ord(character)]

                if len(action) == 8:

                        print '%s' % action

                        if action[6] == '02' and action[7] == '00': # D-Pad
                                if action[4] == 'FF' and action[5] == '7F':
                                         data = 'rr'
#                                        Toy_TrunRight()
                                elif action[4] == '01' and action[5] == '80':
                                         data = 'll'
#                                        Toy_TurnLeft()
#                                else:
#                                         Stop()

                        elif action[6] == '02' and action[7] == '01': # D-Pad
                                if action[4] == 'FF' and action[5] == '7F':
                                         data = 'bb'
#                                        Toy_Backward()
                                elif action[4] == '01' and action[5] == '80':
                                         data = 'ff'
#                                        Toy_Forward()
#                                else:
#                                         Stop()

                        elif action[6] == '01' and action[7] == '01': # Button
                                print ('Speed Change !!! ')
                                print ('befor pwm = '+ str(pwm_value))
                                pwm_value += 1
                                if pwm_value > 4:
                                    pwm_value = 0
                                print ('current pwm = '+ str(pwm_value))
                                pwm2.ChangeDutyCycle(pwm_value*25)



#    while 1:
#        for character in pipe.read(1):
#                action += ['%02X' % ord(character)]
#                if len(action) == 8:

#                        num = int(action[5], 16) # Translate back to integer form
#                        percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] # Calculate the percentage of push
#                        percent128 = str((float(num)/127.0))[2:4]

#                        if percent254 == '.0':
#                                percent254 = '100'
#                        if percent128 == '0':
#                                percent128 = '100'

#                        if action[6] == '01': # Button
#                                if action[4] == '01':
#                                        print 'You pressed button: ' + action[7]
#                                        if action[7] == '09': # Start Button
#                                            data = 'ee'
#                                        elif action[7] == '08': # Start Button
#                                            data = 'dd'
#                                else:
#                                        print 'You released button: ' + action[7]

#                        elif action[7] == '00': # D-pad left/right
#                                if action[4] == 'FF':
#                                        print 'You pressed right on the D-pad'
#                                        data = 'rr'
#                                elif action[4] == '01':
#                                        print 'You pressed left on the D-pad'
#                                        data = 'll'
#                                else:
#                                        print 'You released the D-pad'
#                                        data = 'rl'


#                        elif action[7] == '01': # D-pad up/down
#                                if action[4] == 'FF':
#                                        print 'You pressed down on the D-pad'
#                                        data = 'bb'
#                                elif action[4] == '01':
#                                        print  'You pressed up on the D-pad'
#                                        data = 'ff'
#                                else:
#                                        print 'You released the D-pad'
#                                        data = 'bf'


#                        elif action[7] == '04': # Left Joystick left/right
#                                if action[4] == 'FF':
#                                        print 'You pressed right on the left joystick'
#                                elif action[4] == '01':
#                                        print 'You pressed left on the left joystick'
#                                else:
#                                        print 'You released the left joystick'

#                        elif action[7] == '05': # Left Joystick up/down
#                                if action[4] == 'FF':
#                                        print 'You pressed down on the left joystick'
#                                elif action[4] == '01':
#                                        print 'You pressed up on the left joystick'
#                                else:
#                                        print 'You released the left joystick'

#                        elif action[7] == '02': # Right Joystick left/right
#                                num = int(action[5], 16) # Translate back into integer form
#                                if num >= 128:
#                                        print 'You moved the right joystick left to %' + percent254
#                                elif num <= 127 \
#                                and num != 0:
#                                        print 'You moved the right joystick right to %' + percent128
#                                else:
#                                        print 'You stopped moving the right joystick'

#                        elif action[7] == '03': # Right Joystick up/ down
#                                if num >= 128:
#                                        print 'You moved the right joystick upward to %' + percent254
#                                elif num <= 127 \
#                                and num != 0:
#                                        print 'You moved the right joystick downward to %' + percent128
#                                else:
#                                        print 'You stopped moving the right joystick'

                        action = []

                        if data != ' ':
                            print 'if data : %s' % data
                            data_send(data)

def joyinit():
    for character in pipe.read(1):
        print ''

def data_send(data):
    print 'Here Data : %s' % data
    send_data = 'rcpi' + data + '          '
    s.send(send_data)

if __name__ == "__main__":
    main()
