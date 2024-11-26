#Перевести изображение в hsv

import cv2

image = cv2.imread('image.jpg')  

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('Image', hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()