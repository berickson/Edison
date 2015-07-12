import cv2
import numpy as np
import matplotlib.pyplot as plt


def find_circles(img):
    img = cv2.medianBlur(img,5)

    circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=40,minRadius=10,maxRadius=300)
    #circles = cv2.HoughCircles( img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20)
    
    if circles is None:
        return []
    print circles
    for circle in circles:
        print str(circle)
    return circles[0]


def main():
  print 'main here.'


def capture_image():
    cap = cv2.VideoCapture(0)
    f, img = cap.read()
    cap.release()
    cv2.imwrite('balltest.png', img)
    return img


def draw_circles(img, circles):
    if(circles == None): 
        return
    for circle in circles:
       x, y, r = circle
       cv2.circle(img, (x, y), r, color = (0,0,255))


def show(images) :
    l = len(images)
    fig = plt.figure()
    fig.set_size_inches(20,20)
    for i,image in enumerate(images):
        b,g,r = cv2.split(image)       # get b,g,r
        rgb_img = cv2.merge([r,g,b])     # switch it to rgb

        fig.add_subplot(1, l, i+1)
        plt.imshow(rgb_img)
    plt.show()

def hue_as_gray(grb):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    return h


if __name__ == '__main__':
    main()
    #img = capture_image()
    cap = cv2.VideoCapture(0)
    while True:
         
        #img = cv2.imread('balltest.png')
        f, img = cap.read()
        if not f:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #gray = hue_as_gray(img)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        circles = find_circles(blur)
        draw_circles(img, circles)
        cv2.imshow('circles', img)

        if cv2.waitKey(1) <> -1:
            break;
        #show([img])
    cap.release()
