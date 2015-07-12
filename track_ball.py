#!/usr/bin/python2.7

import cv2
import numpy as np
import sys
#import matplotlib.pyplot as plt

def mean_hsv(im):
    hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    mean_h = np.mean(h)#sum(h)/len(h)
    mean_s = np.mean(s)#sum(s)/len(s)
    mean_v = np.mean(v)#sum(v)/len(v)
    return int(mean_h), int(mean_s), int(mean_v)

def show(im, wait=1):
    fast = True
    cv2.imshow('tracker',im)
    if(fast): wait = 1
    cv2.waitKey(wait)

def show_progress():
    print '.',
    sys.stdout.flush()


# returns values between 0 and 255 within tolerance of v
def range_255_scalar(v, tolerance):
   return max(v-tolerance,0), min(v+tolerance,255)

def range_255(v, tolerance):
    v_min = list()
    v_max = list()
    for i in range(len(v)):
        a,b = range_255_scalar(v[i],tolerance[i])
        v_min.append(a)
        v_max.append(b)
    return tuple(v_min), tuple(v_max)


# see http://www.learnopencv.com/blob-detection-using-opencv-python-c/
def get_blobs(im):
    # Set up the detector with default parameters.
    params = cv2.SimpleBlobDetector_Params()
    params.minArea = 20
    params.filterByArea = False
    params.maxArea = 10000000
    params.filterByCircularity = False
    params.filterByColor = False
    params.filterByInertia = False
    params.filterByConvexity = False

    detector = cv2.SimpleBlobDetector(params)


    # Detect blobs.
    keypoints = detector.detect(im)
#    for k in keypoints: print 'point: {0}, size: {1}'.format(k.pt, k.size)
    return keypoints

def do_contours(threshold):
    contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(threshold, contours, -1, (0,255,0), 3)
    return threshold

def draw_blobs(im, keypoints, color = (255,0,0)):
    return cv2.drawKeypoints(im, keypoints, np.array([]), color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


def smooth(img, size = 10):
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
    im2 = cv2.erode(img, k)
    im3 = cv2.dilate(im2, k)
    return im3

# finds ball based on hsv in image
def find_ball(im, hsv):

    # get threshold image based by color
    blur = cv2.blur(im,(50,50))
    hsv_tolerance = (30,100,150)
    hsv_min, hsv_max = range_255(hsv,hsv_tolerance)
    hsv_min = (hsv_min[0],100,100)
    hsv_max = (hsv_max[0],255,255)
    #print hsv_min, hsv_max
    im_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    im_threshold = cv2.inRange(im_hsv, hsv_min,hsv_max)#(140,100,100), (180,255,255))
    im_threshold = smooth(im_threshold)

    contours, hierarchy = cv2.findContours(im_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print 'countour count: '+str(len(contours))
    #print contours
    #cv2.drawContours(im, contours, -1, (0,255,0), 3)

    # find largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    largest=contours[max_index]
    convex = cv2.convexHull(largest)

    x,y,w,h = cv2.boundingRect(convex)
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255))

    #cv2.drawContours(im, [largest], -1, (255,0,0), 3)
    #cv2.drawContours(im, [convex], -1, (0,0,255), 3)


def main():
    cap = cv2.VideoCapture('input/ball_to_track_1.mov')

    # get average hsv of first frame
    # on the car, this will be button push 1
    rv,im = cap.read()
    mean = mean_hsv(im)
    print mean
#    show(im,5000)

    # locate and get size of ball after 5 seconds
    # on the car, this will be button push 2
    cap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, 5000)
    while(True):
        rv,im = cap.read()
        if not rv: break
        find_ball(im, mean)
        show(im,50000)



main()
