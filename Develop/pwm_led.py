#!/usr/bin/python3

import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time

print("LED DIMMER USING PULSE WIDTH MODULATION")

GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
GPIO.setup(25, GPIO.OUT) # GPIO 25 is set to be an output.

pwm = GPIO.PWM(25, 10)   # pwm is an object. This gives a neat way to control the pin.
                         # 25 is the BCM pin number.
                         # 10 is the frequency in Hz.

print("50%")             # Display 50 on the screen
pwm.start(50)            # This 50 is the mark/space ratio or duty cycle of 50%
                         # Values from 0 to 100 are allowed including numbers like 33.33
time.sleep(3)            # Three seconds till the next change

pwm.ChangeFrequency(50)  # Frequency is now 50 Hz - LED stops flickering

print("5%")
pwm.ChangeDutyCycle(5)   # Duty cycle is now 5%
time.sleep(0.5)          # 0.5 seconds till the next change

print("10%")
pwm.ChangeDutyCycle(10)  # Duty cycle is now 10%
time.sleep(0.5)          # 0.5 seconds till the next change

print("15%")
pwm.ChangeDutyCycle(15)  # Duty cycle is now 15%
time.sleep(0.5)          # 0.5 seconds till the next change

print("20%")
pwm.ChangeDutyCycle(20)  # Duty cycle is now 20%
time.sleep(0.5)          # 0.5 seconds till the next change

print("30%")
pwm.ChangeDutyCycle(30)  # Duty cycle is now 30%
time.sleep(0.5)          # 0.5 seconds till the next change

print("50%")
pwm.ChangeDutyCycle(50)  # Duty cycle is now 50%
time.sleep(0.5)          # 0.5 seconds till the next change

print("80%")
pwm.ChangeDutyCycle(80)  # Duty cycle is now 80%
time.sleep(0.5)          # 0.5 seconds till the next change

print("100%")
pwm.ChangeDutyCycle(100) # Duty cycle is now 100%
time.sleep(0.5)          # 0.5 seconds till the next change

print("50 at 5.5Hz for 3 seconds")
pwm.ChangeFrequency(5.5) # Frequency is now 5.5 Hz
pwm.ChangeDutyCycle(50)  # Duty cycle is now 50%
time.sleep(3)            # Three seconds till the next change

pwm.stop()               # Turn PWM off

GPIO.cleanup()           # Always clean up at the end of programs.
