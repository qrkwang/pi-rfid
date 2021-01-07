#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

time.sleep(10)
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        with open('rfid.txt', 'w+') as the_file:
            the_file.write(text)
        time.sleep(0.5)
finally:
        GPIO.cleanup()
