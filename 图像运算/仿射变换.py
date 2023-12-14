import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./2.jpg")
rows, cols = img.shape[:2]
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[100,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1, pts2)
res = cv.warpAffine(img, M, (cols,rows))
cv.imshow('1',res[:,:,::-1])
cv.waitKey(0)
cv.destroyAllWindows()