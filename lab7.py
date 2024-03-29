import cv2
# import Numpy
import numpy as np

# read an image using imread
img = cv2.imread('hi.jpg', 0)
cv2.imshow('input', img)

# creating a Histograms Equalization
# of an image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
# res = np.hstack((img, equ))

# show image input vs output
cv2.imshow('output', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
