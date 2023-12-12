import cv2 as cv
import numpy as np

# 产生高斯噪声
def AddGaussNoise(src,sigma):
    mean = 0
    # 获取图片的高度和宽度
    height, width, channels = src.shape[0:3]
    gauss = np.random.normal(mean,sigma,(height,width,channels))
    noisy_img = np.uint8(src + gauss)
    return noisy_img

img = cv.imread("1.png")
noise = AddGaussNoise(img,10)
bulr = cv.GaussianBlur(noise, (3,3), 1)
# 按任意键退出图片显示
cv.imshow('1', noise)
cv.imshow('2', bulr)
cv.waitKey()