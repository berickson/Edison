#!/usr/bin/python2.7
import mraa
import time
led=mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
delay_sec = 1.0 
while True:
  led.write(1)
  time.sleep(delay_sec)
  led.write(0)
  time.sleep(delay_sec)

