import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#灰度图
img = cv.imread("1.png", 0)
res = cv.calcHist(img, [0], None, [256],[0,256])
plt.imshow(img, cmap=plt.cm.gray)
plt.figure(figsize=(10,6))
plt.plot(res)
cv.waitKey()