#!/usr/bin/python2.7
import cv2
from datetime import datetime
camCount = 2
lo_res = False
cam = [0,0]
s = [0,0]
img = [0,0]
for n in range(camCount):
  cam[n] = cv2.VideoCapture(n)
  if lo_res:
    cam[n].set(3,240)
    cam[n].set(4,320)
for t in range(1):
  print t
  for n in range(camCount):
    s[n], img[n] = cam[n].read()
for n in range(camCount):
  if s[n]: #read without errors
    time_string = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    filename = '/media/sdcard/im{0}-{1}.jpeg'.format(time_string,n)
    cv2.imwrite(filename, img[n])
  else:
      print 'error reading camera'
      print s

