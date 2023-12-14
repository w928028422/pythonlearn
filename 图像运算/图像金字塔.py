import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./1.jpg")
rows, cols = img.shape[:2]
cv.imshow('1',img[:,:,::-1])
up = cv.pyrUp(img)
cv.imshow('up',up[:,:,::-1])
down = cv.pyrDown(img)
cv.imshow('down',down[:,:,::-1])
cv.waitKey(0)
cv.destroyAllWindows()