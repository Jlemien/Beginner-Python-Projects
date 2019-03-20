import cv2
import matplotlib.pyplot as plt
import numpy as np

inputImageLocation = r"C:\Users\Josep\Pictures\Art Images for teacherspayteachers.com\The Starry Night - Vincent van Gogh - Smaller.jpg"
img = cv2.imread(inputImageLocation, cv2.IMREAD_COLOR)
#IMREAD_COLOR
#IMREAD_UNCHANGED

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.line(img, (0,0),(150,150), (255,255,255),15)
#cv2.rectangle(img,  (15,25),(200,150),(0,255,0), 5)
#cv2.circle(img, (100,63), 55, (0,0,255), -1)

#pts = np.array([[100,500],[200,300],[700,200],[200,110]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img, [pts], True, (0,255,255), 3)

#lorum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at pellentesque justo, vitae rhoncus tellus. Vivamus sit amet nisi tellus. Nulla quis molestie libero. In viverra luctus ornare. Duis scelerisque libero eu sapien luctus semper. Nullam sollicitudin ipsum eget nunc consequat pharetra. Pellentesque auctor enim malesuada tortor aliquet posuere. Sed viverra ullamcorper lacus at laoreet. Aliquam a odio feugiat tellus sodales viverra. Nulla rhoncus consectetur orci eget ullamcorper. Duis lobortis eros est, tristique facilisis risus ornare eget. Mauris eu dictum turpis. Quisque vulputate, nisl lobortis ultrices porttitor, augue odio bibendum dui, sed eleifend quam ligula et urna. Mauris rhoncus egestas arcu, a fermentum ex faucibus commodo."
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img, "Event Name", (0,150), font, 5, (255,200,200), 5, cv2.LINE_AA)
#cv2.putText(img, "Date & Time", (0,250), font, 3, (255,255,255), 3, cv2.LINE_AA)
#cv2.putText(img, "Location", (0,350), font, 3, (255,255,255), 3, cv2.LINE_AA)
#cv2.putText(img, lorum, (0,600), font, 1, (0,0,255), 1, cv2.LINE_AA)


#this is how I can "copy and paste" a part of an image
watch_face = img[50:100, 50:100]
img[50:100,110:160] = watch_face

#I can easily set certain parts of it to white
img[50:100, 50:100] = [255,255,255]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#beginings of TeachersPayTeachers worksheet automater
#step 1: import image
#step 2: figure out image width and height
#step 3: scale image so that it can be printed on an A4 page
#step4:
    # randomly select a shape (circles and squares at the beginner level, polygons at higher levels)
    # randomly select a location (make sure it is not overlapping with the location of another shape)
    # copy the image content to a variable
    # set the shape (with a line width of -1 and a color of white) in the image
    # set the variable (eith the image content) on the side of the sheet


