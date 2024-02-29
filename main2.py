import cv2
import numpy as np

image1=cv2.imread("Ash.png")
image2=cv2.imread("pikachu.png")

sub=cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', sub)

cv2.waitKey(0)
cv2.destroyAllWindows()