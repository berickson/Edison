#!/usr/bin/python2.7
import threading
import mraa
import time

led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
delay_sec = 1.0 


def blink():
  while True:
    led.write(1)
    time.sleep(delay_sec)
    led.write(0)
    time.sleep(delay_sec)

blink_thread = threading.Thread(name='blink',target=blink)
blink_thread.daemon = True
blink_thread.start()
while(delay_sec >= 0):
  delay_sec = input('enter blink rate in seconds, negative to quit: ');

