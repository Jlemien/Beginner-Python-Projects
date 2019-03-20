import numpy as np
import cv2
import random

# Load an color image in grayscale
img = cv2.imread(r"C:\Users\Josep\Pictures\Art Images for teacherspayteachers.com\The Starry Night - Vincent van Gogh - Smaller.jpg",1)

# Create a black image
#img = np.zeros((512,512,3), np.uint8)

#get the dimensions of the image
#(height, width) = (img.shape)
#print(height)
#print(width)

# This is how to A) add borders, and B) add a space off to the side where I can place the shapes
top, bottom, left, right = [10]*4
right = 200
img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

#cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# A randomized triangle
#min = 1
#max = 200
#pts = np.array([[random.randint(min,max),random.randint(min,max)],[random.randint(min,max),random.randint(min,max)],[random.randint(min,max),random.randint(min,max)]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img,[pts],True,(0,255,255))


cv2.imshow('image',img_with_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This is how I can save the image
#cv2.imwrite('C:\Users\Josep\Desktop\New image.png',img)


