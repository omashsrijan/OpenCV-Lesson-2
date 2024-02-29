import cv2
import numpy as np

img=cv2.imread("pikachu.png",1)
cv2.imshow("Original Image", img)

#Order of dimensions is (WIDTH,HEIGHT)
resized=cv2.resize(img, (500,250))
cv2.imshow("Resized Image", resized)

cv2.waitKey(delay=5000)
cv2.destroyAllWindows()