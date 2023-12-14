import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./1.jpg")
rows, cols = img.shape[:2]
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,145],[300,100],[80,290],[310,300]])
M = cv.getPerspectiveTransform(pts1, pts2)
res = cv.warpPerspective(img, M, (cols,rows))
cv.imshow('1',res[:,:,::-1])
cv.waitKey(0)
cv.destroyAllWindows()