import RPi.GPIO as GPIO
from time import sleep

ENABLE_PIN1 = 18
ENABLE_PIN2 = 13
IN1 = 24
IN2 = 23
IN3 = 21
IN4 = 20
ENGINE_FREQ1 = 300
ENGINE_FREQ2 = 300

enable_pin1 = ENABLE_PIN1
enable_pin2 = ENABLE_PIN2
in1_pin = IN1
in2_pin = IN2
in3_pin = IN3
in4_pin = IN4

GPIO.setmode(GPIO.BCM)

GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)
GPIO.setup(in3_pin, GPIO.OUT)
GPIO.setup(in4_pin, GPIO.OUT)

pwm1 = GPIO.PWM(enable_pin1, ENGINE_FREQ1)
pwm2 = GPIO.PWM(enable_pin2, ENGINE_FREQ2)

def 2WD_Forward():

    pwm1.start(0)
    pwm2.start(0)

    print "GO Forward"    
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    GPIO.output(in3_pin, False)
    GPIO.output(in4_pin, True)
    pwm1.ChangeDutyCycle(30)
    pwm2.ChangeDutyCycle(30)

def 2WD_Backward():
    pwm1.start(0)
    pwm2.start(0)

    print "GO backward"
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)
    GPIO.output(in3_pin, True)
    GPIO.output(in4_pin, False)

    pwm1.ChangeDutyCycle(30)
    pwm2.ChangeDutyCycle(30)	

def 2WD_TurnLeft():
    pwm1.start(0)
    pwm2.start(0)

    print "GO TurnLeft"
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    GPIO.output(in3_pin, False)
    GPIO.output(in4_pin, True)

    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(10)

def 2WD_TurnRight():
    pwm1.start(0)
    pwm2.start(0)

    print "GO TurnRight"
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    GPIO.output(in3_pin, False)
    GPIO.output(in4_pin, True)

    pwm1.ChangeDutyCycle(10)
    pwm2.ChangeDutyCycle(100)

def 2WD_Stop():
    pwm1.start(0)
    pwm2.start(0)
