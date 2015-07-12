#!/usr/bin/python2.7

# 
# A typical servo motor expects to be updated every 20 ms
# with a pulse between 1ms and 2ms
# With a 1 ms pulse, the servo will be at the 0 degree position
# and with a 2 ms pulse, the servo will be at 180 degrees.
#
# trials with Parallax standard servo
# show actual ranges were 300 to 2000 us pulse width
# that were responded to

import mraa
import time
pin = 3
period_ms = 30
min_pulse_us = 1400 
max_pulse_us = 1450
pulse_us_delta = 1
x = mraa.Pwm(pin)
x.period_ms(period_ms)
x.pulsewidth_us(min_pulse_us)
x.enable(True)
print 'set pin={0} period={1}ms'.format(pin,period_ms) 

pulse_us = min_pulse_us
while True:
  pulse_us = input('Enter pulse us: ')
  print 'setting pulse time to {0} us'.format(pulse_us)
  x.pulsewidth_us(pulse_us)
  time.sleep(0.5)
  pulse_us += pulse_us_delta
  if pulse_us >= max_pulse_us:
    pulse_us = min_pulse_us
