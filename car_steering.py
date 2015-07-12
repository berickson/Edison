#!/usr/bin/python2.7

import mraa
import time
pin = 5
period_ms = 20
x = mraa.Pwm(pin)
x.period_ms(period_ms)
x.enable(True)
print 'set pin={0} period={1}ms'.format(pin,period_ms) 

while True:
  print '800=rightmost 1300=straight 1800=leftmost'
  pulse_us = input('enter pulse_us: ')
  print 'setting pulse time to {0} us'.format(pulse_us)
  x.pulsewidth_us(pulse_us)
