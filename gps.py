#!/usr/bin/python2.7
import serial
import time
import pynmea2
import sys
from datetime import datetime

def append_to_file(name, text):
  with open(name, "a") as f:
    f.write(text)

# prints out points you can plot at http://www.hamstermap.com/quickmap.php
def main():
  time_string = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
  filename = '/media/sdcard/gps{0}.csv'.format(time_string)
  raw_filename = '/media/sdcard/rawgps{0}.csv'.format(time_string)
  
  print 'logging to the following files'
  print filename
  print raw_filename
  ser = serial.Serial('/dev/ttyMFD1', 9600)

  while(True):
    s = ser.readline()

    if(s.startswith("$GP")):
      
      append_to_file(raw_filename, s)
      try:
        msg = pynmea2.parse(s)
      except pynmea2.nmea.ParseError:
        continue
    
      if msg.sentence_type == 'RMC':
        s = '{0},{1},{2}\n'.format(
          msg.datetime, 
          msg.latitude, 
          msg.longitude)
        append_to_file(filename, s)


if __name__ == "__main__":
  main()
