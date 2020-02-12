import cv2
import numpy as np
import imutils
tri=125
image=cv2.imread('park7.jpg')
#cv2.imshow('show',image)
#cv2.waitKey(0)
image=cv2.resize(image,(800,600))

im_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#for parking image
#_,im_thresh=cv2.threshold(im_gray,40,255,cv2.THRESH_BINARY_INV)

#for car image
#_,im_thresh=cv2.threshold(im_gray,150,255,cv2.THRESH_BINARY)
#_,im_thresh=cv2.threshold(im_gray,125,255,cv2.THRESH_BINARY_INV)#best value
_,im_thresh=cv2.threshold(im_gray,tri,255,cv2.THRESH_BINARY_INV)#trial
kernel = np.ones((0,0), np.uint8) 
im_erode = cv2.erode(im_thresh, kernel, iterations=1)
cv2.imshow('im_gray',im_gray)
cv2.imshow('im_thresh',im_thresh)
cv2.imshow('im_erode',im_erode)
cv2.waitKey(0)


ref_image=cv2.imread('parking7.jpg')

ref_image=cv2.resize(ref_image,(800,600))

ref_im_gray=cv2.cvtColor(ref_image,cv2.COLOR_BGR2GRAY)


_,ref_im_thresh=cv2.threshold(ref_im_gray,tri,255,cv2.THRESH_BINARY)#best value

 
ref_im_erode = cv2.erode(ref_im_thresh, kernel, iterations=1)


cv2.imshow('ref_im_gray',ref_im_gray)
cv2.imshow('ref_im_thresh',ref_im_thresh)

cv2.waitKey(0)
#mask = cv2.bitwise_and(ref_im_thresh,im_thresh)
mask = cv2.bitwise_and(ref_im_erode,im_erode)

mask2=mask
_,mask_contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


  
cnts = sorted(mask_contours, key=lambda x: cv2.contourArea(x), reverse = True)
for a in cnts:
	print(cv2.contourArea(a))

j=1
color=1
font = cv2.FONT_HERSHEY_SIMPLEX
for i in cnts:
	[x,y,w,h]=cv2.boundingRect(i)
	
	j=j+1
	
	if w>50:
		print('iteration',j)
		print('x',x)
		print('y',y)
		print('w',w)
		print('h',h)
		cv2.drawContours(image, i, -1, (0, 255, 0), 3)
		cv2.rectangle(image,(x,y),(x+w,y+h),(color,color,color),2)
		cv2.putText(image,str(j),(x,y), font, 1,(color,color,color),2,cv2.LINE_AA)
		color=color+10
	

#cv2.drawContours(image, mask_contours, -1, (0,140,0), 3)
cv2.imshow('ref_im_gray',ref_im_gray)
cv2.imshow('ref_im_thresh',ref_im_thresh)
cv2.imshow('mask',mask)
cv2.imshow('image',image)
#cv2.imshow('mask_contours',mask_contours)



cv2.waitKey(0)


