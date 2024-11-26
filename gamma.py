#Сделать гамма-перобразование

import cv2
import numpy as np

def gamma_correction(image, gamma):
    normalized_image = image / 255.0
    gamma_corrected = np.power(normalized_image, gamma)
    gamma_corrected = np.uint8(gamma_corrected * 255)
    return gamma_corrected

image = cv2.imread('image.jpg')  

gamma_value = 2 

gamma_corrected_image = gamma_correction(image, gamma_value)

cv2.imshow('Image', gamma_corrected_image)

cv2.waitKey(0)
cv2.destroyAllWindows()