#!/usr/bin/python2.7

import mraa
import time
pin = 3
period_ms = 20

pulse_us = 0  # neutral
x = mraa.Pwm(pin)
x.period_ms(period_ms)
x.enable(True)

print 'set pin={0} period={1}ms'.format(pin,period_ms) 

while True:
  x.pulsewidth_us(pulse_us)
  print 'setting pulse time to {0} us'.format(pulse_us)
  print '0=neutral 1330=slow_forward 1415=slow_reverse'
  pulse_us = input('enter pulse_us: ')
