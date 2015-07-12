#!/usr/bin/python2.7

import mraa
import time

# Dummy class allows creating objects with dynamic members
class Object(object):
  pass
  
class Car():
  def __init__(self):
    self.pins = Object()
    self.pins.steering = 5
    self.pins.power = 3
    self.period_ms = 20
    
    self.steering_pwm = mraa.Pwm(self.pins.steering)
    self.steering_pwm.period_ms(self.period_ms)
    self.steering_pwm.enable(True)

    self.speed_pwm = mraa.Pwm(self.pins.power)
    self.speed_pwm.period_ms(self.period_ms)
    self.speed_pwm.enable(True)

    
  # direction leftmost = -1.0  center = 0.0 righmost = 1.0 
  def steer(self, direction):
    print 'steer: {0}'.format(direction)
    
    direction = float(direction)
    if(abs(direction) > 1.01):
      raise ValueError("direction must be between -1.0 and 1.0")
    # pulse_us 800=rightmost 1300=straight 1800=leftmost
    pulse_us = 1300. - (direction * 500.0)
    self.steering_pwm.pulsewidth_us( int(pulse_us) )
  
  # speed full_reverse = -1.0  stop = 0.0 full_forward = 1.0
  # 
  # note: you must stop before changing direction
  #
  # 1412 - slow reverse
  # 1334 - slow forward  
  def set_speed(self, speed):
    print 'set_speed: {0}'.format(speed)
    speed = float(speed)
    if(abs(speed) > 1.01):
      raise ValueError("speed must be between -1.0 and 1.0")
    #if(abs(speed) < 0.01):
    #  self.stop()
    #  return
    pulse_us = int(1375. - (300. * speed))
    print 'pulse_us: {0}'.format(pulse_us)
    self.speed_pwm.pulsewidth_us(pulse_us)

  def stop(self):
    print 'stop'
    self.speed_pwm.pulsewidth_us(0)

  def reset(self):
    print 'reset'
    self.steer(0.0)

def test_steering(car, directions = [0,0.5,1.0,0.5,0,-0.5,-1.,-0.5,0]):
  for direction in directions:
    car.steer(direction)
    time.sleep(1)

def test_speed(car, speeds=[0,0.2,-0.2,0,-0.2,0]):
  car = Car()
  for speed in speeds:
    car.set_speed(1.0*speed)
    time.sleep(1)
    
def main():
  car = Car()
  test_steering(car)
  test_speed(car)
  car.reset()

if __name__ == "__main__":
  main()
