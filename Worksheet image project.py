import numpy as np
import cv2
import random

# Load an color image
img = cv2.imread(r"C:\Users\Josep\Pictures\Art Images for teacherspayteachers.com\The Starry Night - Vincent van Gogh - Smaller.jpg",1)

# get the dimensions of the image
(height, width, channels) = (img.shape)
print(height)
print(width)

# This is how to A) add borders, and B) add a space off to the side where I can place the shapes
top, bottom, left, right = [10]*4
right = 200
img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

(height, width, channels) = (img_with_border.shape)
print(height)
print(width)

# A randomized triangle
#min = 1
#max = 200
#pts = np.array([[random.randint(min,max),random.randint(min,max)],[random.randint(min,max),random.randint(min,max)],[random.randint(min,max),random.randint(min,max)]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img,[pts],True,(0,255,255))

# A rectangle
#cv2.rectangle(img,  (15,25),(200,150),(0,255,0), 5)

# A circle
#cv2.circle(img, (100,63), 55, (0,0,255), -1)

#this is how I can "copy and paste" a part of an image
watch_face = img_with_border[50:100, 50:100]
img_with_border[50:100,710:760] = watch_face

#I can easily set certain parts of it to white
#img_with_border[50:100, 50:100] = [255,255,255]
img_with_border[50:100, 50:100] = [255,255,255]

# This is how to show the image on the screen
cv2.imshow('image',img_with_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This is how I can save the image
#cv2.imwrite('C:\Users\Josep\Desktop\New image.png',img)


