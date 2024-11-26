# Сделать бинаризацию изображения

import cv2
import numpy as np

image = cv2.imread('image.jpg')

threshold_value = 127
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('Image', binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()