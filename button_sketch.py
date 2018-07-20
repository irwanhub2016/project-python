#!/bin/python

import RPi.GPIO as GPIO
import os

gpio_pin_number=YOUR_CHOSEN_GPIO_NUMBER_HERE

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    print("Shutdown is starting ...")
    os.system("sudo shutdown -h now")
except:
    pass

GPIO.cleanup()
