Adafruit Python SSD1306
=======================

Python library to use SSD1306-based 128x64 or 128x32 pixel OLED displays with a Raspberry Pi or Beaglebone Black.

Designed specifically to work with the Adafruit SSD1306-based OLED displays ----> https://www.adafruit.com/categories/98

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.
MIT license, all text above must be included in any redistribution

# RAS RC Car Project 

<img src="https://github.com/rasplay/RAS_RC_CAR_Project/blob/master/img/I2C_OLED_3.jpg" width="700">

## How To Wiring with RapsberryPi GPIO

<img src="https://cdn-learn.adafruit.com/assets/assets/000/017/603/large1024/raspberry_pi_RaspberryPi_I2C_bb.png" width="700">

* Connect display ground to Raspberry Pi ground (black wire).
* Connect display VIN to Raspberry Pi 3.3 volt (red wire).
* Connect display RST to Raspberry Pi GPIO 24 (blue wire). You can alternatively use any free digital GPIO pin for the reset pin.
* Connect display SCL to Raspberry Pi SCL (purple wire).
* Connect display SDA to Raspberry Pi SDA (orange wire).

## How to Install SoftWare

### Source Download through ours project github

```
$ git clone https://github.com/rasplay/RAS_RC_CAR_Project
```

```
$ cd RAS_RC_CAR_Project/I2C_OLDE/Adafruit_SSD1306
```


### Install about python modules

```
$ sudo apt-get install build-essential python-dev python-pip
```

### Install python Imaging Library

```
$ sudo apt-get install python-imaging python-smbus
```

### Install python oled module

```
$ sudo apt-get install python-imaging python-smbus
```

### Enable I2C on GUI MODE

<img src="https://github.com/rasplay/RAS_RC_CAR_Project/blob/master/img/I2C_OLED_1.png" width="700">
<img src="https://github.com/rasplay/RAS_RC_CAR_Project/blob/master/img/I2C_OLED_2.png" width="700">

### I2C Adress check

```
$ sudo i2cdetect -y 1
```
<img src="https://cdn-learn.adafruit.com/assets/assets/000/042/244/medium800/adafruit_products_i2c.png" width="700">


### Run oled image view 

```
$ cd examples
```

```
$ sudo python images.py
```



