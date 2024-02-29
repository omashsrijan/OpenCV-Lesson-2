import cv2
import numpy as np

img=cv2.imread("pikachu.png")
cv2.imshow("Original Image", img)

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
#(img, Kernal_size ,std_dev)
Gaussian=cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gausssian Blur", Gaussian)

# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.
#(img,Kernal_size)
Median=cv2.medianBlur(img, 5)
cv2.imshow("Median Blur", Median)

# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)
Bilateral=cv2.bilateralFilter(img, 9,75,75)
cv2.imshow("Bilateral Blur", Bilateral)

cv2.waitKey(delay=5000)
cv2.destroyAllWindows()