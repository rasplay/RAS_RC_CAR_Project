<img src="https://github.com/rasplay/RAS_RC_CAR/blob/master/img/RASTA_RC_remodel2.jpg" width="1200">
<img src="https://github.com/rasplay/RAS_RC_CAR/blob/master/img/RAS_RC.jpg" width="1200">

### RAS_RC_Version 5.0 Update by Multi Controller RC of RaspberryPi Village.

```
This Original Source is update 5.0 version  of Multi Controller RC for RaspberryPi Village.
OpenMake will be support library funciton of RC Car Controller Software and makers can use function in file.
```
※ We will are often update many function through here and Document write manual that how to use library function.

***

### RAS RC-Car support controller 

* Support General USB Keyboard
* Support General USB GAMEPAD contoroller
* Support General USB Joystick contoroller
* Support Bluetooth Xiaomi Joystick contoroller
* Spport Speed Control(4 Step)

### Develop folder Description : RAS RC CAR TEST Source 

> This folder is test source add new function ago at the RAS RC CAR sources.

### Attach File Description

* **RAS_RC_Motor_RASTA.py** : RASTA Toy RC Car Motor Control file
* **RAS_RC_Motor_2WD.py** : 2WD RC Car Motor Control file
* **pwm_kbd.py** : RC Car Control by Keyboard through SSH
* **pad_usb.py** : RC Car Control by USB GAMEPAD Joystick(4step speed control)
* ~~**pwm_joy_xiaomi.py** : RC Car Control by Xiaomi Bluetooth Joystick~~
* **joy_xaomi.py** : RC Car Control by Xiaomi Bluetooth Joystick(4step speed control)
  <img src="https://github.com/rasplay/RAS_RC_CAR_Project/blob/master/img/xiomi_pad.jpg" width="450">

***

### RAS RC-Car has been used RaspberryPi GPIO PIN

* **Motor Drive** : SN754410NE 
* **RaspberryPi GPIO**   
   - Motor A : GPIO 20, GPIO 21, GPIO 13(PWM1)
   - Motor B : GPIO 23, GPIO 24, GPIO 18(PWM0)
   - Front LED : GPIO 16
   - Back LED : GPIO 26

***
   
**To Be Continue ...**

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
