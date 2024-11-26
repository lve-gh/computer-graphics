import cv2
import numpy as np

image = cv2.imread('image.jpg') 

b, g, r = cv2.split(image)

b_equalized = cv2.equalizeHist(b)
g_equalized = cv2.equalizeHist(g)
r_equalized = cv2.equalizeHist(r)

equalized_image = cv2.merge((b_equalized, g_equalized, r_equalized))

cv2.imshow('Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()