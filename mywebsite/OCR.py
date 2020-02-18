import cv2
import numpy as np
from PIL import Image
import PIL

image = cv2.imread('image/Test.jpg')
print(image)
# image = cv2.resize(image_original,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
cv2.namedWindow("Image")
#cv2.imshow('Image',image)
# image = cv2.resize(image_original,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)

#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# original_resized = cv2.resize(gray, (0,0), fx=.2, fy=.2)
#cv2.imshow('gray',gray)
#cv2.waitKey(0)

#Remove Salt and pepper noise
saltpep = cv2.fastNlMeansDenoising(gray,None,9,13)
# original_resized = cv2.resize(saltpep, (0,0), fx=.2, fy=.2)
#cv2.imshow('Grayscale',saltpep)
#cv2.waitKey(0)

#blur
blured = cv2.blur(saltpep,(3,3))
# original_resized = cv2.resize(blured, (0,0), fx=.2, fy=.2)
#cv2.imshow('blured',blured)
#cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
# original_resized = cv2.resize(thresh, (0,0), fx=.2, fy=.2)
#cv2.imshow('Threshold',thresh)
#cv2.waitKey(0)

#dilation
kernel = np.ones((5,100), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
# original_resized = cv2.resize(img_dilation, (0,0), fx=.2, fy=.2)
#cv2.imshow('dilated',img_dilation)
#cv2.waitKey(0)

#find contours
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])

#read lines
ctr_word=0
ctr_line=0
for i, ctr in enumerate(sorted_ctrs):
    ctr_line=ctr_line+1

     
    if(ctr_line<4):
        print("test")

    #function compare segment dengan gambar

    if(ctr_line>6):
        break
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    # print (x)
    # print (y)
    # print (w)
    # print (h)

    # Getting ROI
    roi = image[y:y+h, x:x+w]

    ##   show ROI
    #image = image.save(ctr_line + ".jpg")
    
    cv2.imshow('segment no:' +str(i),roi)
    cv2.imwrite(str(i) + " .jpg", roi )
    print(i)
    cv2.waitKey(0)
