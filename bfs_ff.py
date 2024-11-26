# Сделать фильтрацию изображения при помощи преобразования Фурье,
#оставить только быстрые частоты


import cv2
import numpy as np


image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  

rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  


mask = np.ones((rows, cols, 2), np.float32)  
r = 30  
cv2.circle(mask, (ccol, crow), r, (0, 0, 0), -1)  

dft_shift_filtered = dft_shift * mask

idft_shift = np.fft.ifftshift(dft_shift_filtered)
img_back = cv2.idft(idft_shift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
img_back = np.uint8(img_back)

cv2.imshow('Image', img_back)

cv2.waitKey(0)
cv2.destroyAllWindows()