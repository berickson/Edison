#!/usr/bin/python2.7
import cv2
import time
from datetime import datetime
cam = cv2.VideoCapture(0)


s, img = cam.read()
height , width , layers =  img.shape
framerate = 10

# mac compatible codecs  IYUV, I420, PIM1, MJPG, FFV1 and DIVX
# based on http://stackoverflow.com/questions/18835941/unable-to-write-video-using-python-and-opencv2-on-mac-os-x

# this on works on mac!
#video = cv2.VideoWriter('video.mov',cv2.cv.FOURCC('m', 'p', '4', 'v'),framerate,(width,height))


video = cv2.VideoWriter("capture.avi",cv2.cv.FOURCC('D','I','V','X'),framerate,(width,height))

tnext = time.time() + 1./framerate

for _ in range(10):
  s, img = cam.read()
  video.write(img)
  now = time.time()
  if(now < tnext):
    time.sleep(tnext-now)
    print 'sleeping ' + str(tnext-now)
  tnext = tnext + 1./framerate


cv2.destroyAllWindows()
video.release()
