#!/usr/bin/python2.7

import mraa
import time
led=mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
refresh_rate = 0.0001 
portion_on = 0.0001 
while True:
  led.write(1)
#  time.sleep(refresh_rate*portion_on)
  led.write(0)
  time.sleep(refresh_rate*(1.0-portion_on))

