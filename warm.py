# Изменить баланс белого: сделать более "теплую" картинку

import cv2
import numpy as np

def warm_image(image, red_mult, green_mult, blue_mult):
    b, g, r = cv2.split(image)
    r = np.clip(r * red_mult, 0, 255).astype(np.uint8)
    g = np.clip(g * green_mult, 0, 255).astype(np.uint8)
    b = np.clip(b * blue_mult, 0, 255).astype(np.uint8)
    warmed_image = cv2.merge([b, g, r])
    return warmed_image

img = cv2.imread("image.jpg")

warmed_img = warm_image(img, 1.0, 0.6, 0.5)

cv2.imshow("Image", warmed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()