#Изменить яркость изображения

import cv2
import numpy as np

image = cv2.imread('image.jpg')  

brightness_increase = 75

brightened_image = cv2.convertScaleAbs(image, alpha=1, beta=brightness_increase)

cv2.imshow('Image', brightened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
