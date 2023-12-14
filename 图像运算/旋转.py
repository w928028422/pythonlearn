import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./1.jpg")
rows, cols = img.shape[:2]
M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 1)
res = cv.warpAffine(img, M, (cols,rows))
cv.imshow('1',res[:,:,::-1])
cv.waitKey(0)
cv.destroyAllWindows()