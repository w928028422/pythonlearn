import cv2 as cv
import numpy as np

# 产生椒盐噪声
def AddSaltPepperNoise(src, rate):
    srcCopy = src.copy()
    height, width = srcCopy.shape[0:2]
    noiseCount = int(rate*height*width/2)
    # add salt noise
    X = np.random.randint(width,size=(noiseCount,))
    Y = np.random.randint(height,size=(noiseCount,))
    srcCopy[Y, X] = 255
    # add black peper noise
    X = np.random.randint(width,size=(noiseCount,))
    Y = np.random.randint(height,size=(noiseCount,))
    srcCopy[Y, X] = 0
    return srcCopy

img = cv.imread("1.png")
noise = AddSaltPepperNoise(img,0.01)
bulr = cv.medianBlur(noise, 3)
# 按任意键退出图片显示
cv.imshow('1', noise)
cv.imshow('2', bulr)
cv.waitKey()