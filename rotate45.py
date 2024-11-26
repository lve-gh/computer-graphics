# Повернуть изображение на 45 градусов

import cv2
import numpy as np

image = cv2.imread('image.jpg')

height, width, _ = image.shape

center_x = width // 2
center_y = height // 2

rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), 45, 1.0)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
