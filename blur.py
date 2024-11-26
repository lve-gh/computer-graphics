#Сделать размытие изображения

import cv2

img = cv2.imread("image.jpg")

blurred_img = cv2.GaussianBlur(img, (5, 5), 3)

cv2.imshow("Image", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()