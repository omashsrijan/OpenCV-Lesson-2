import cv2
import numpy as np

img=cv2.imread("aang.jfif",1)
cv2.imshow("Original Image", img)

resized=cv2.resize(img, (500,250))
cv2.imshow("Resized Image", resized)

kernel=np.ones((5,5), np.uint8)
print(kernel)
weird=cv2.erode(img,kernel)
cv2.imshow("Eroded Image", weird)

borderedpic=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT, value=1)
cv2.imshow("Bordered Image", borderedpic)

Gaussian=cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gausssian Blur", Gaussian)

Median=cv2.medianBlur(img, 5)
cv2.imshow("Median Blur", Median)

Bilateral=cv2.bilateralFilter(img, 9,75,75)
cv2.imshow("Bilateral Blur", Bilateral)

cv2.waitKey(delay=5000)
cv2.destroyAllWindows()