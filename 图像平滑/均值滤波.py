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

def AddGaussNoise(src,sigma):
    mean = 0
    # 获取图片的高度和宽度
    height, width, channels = src.shape[0:3]
    gauss = np.random.normal(mean,sigma,(height,width,channels))
    noisy_img = np.uint8(src + gauss)
    return noisy_img

img = cv.imread("1.png")
noise1 = AddSaltPepperNoise(img,0.01)
noise2 = AddGaussNoise(img, 5)
bulr1 = cv.blur(noise1, (3,3))
bulr2 = cv.blur(noise2, (3,3))
# 按任意键退出图片显示
cv.imshow('1', noise1)
cv.imshow('2', noise2)
cv.imshow('3', bulr1)
cv.imshow('4', bulr2)
cv.waitKey()