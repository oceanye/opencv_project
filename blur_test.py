import numpy as np
import random
import cv2 as cv

def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def filter2D_demo(src):

    # 当kernel总和为 1 时：增强锐化
    # 当kernel总和为 0 时：边缘梯度
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(src, -1, kernel=kernel)
    cv.imshow("dst", dst)

img = cv.imread("./1.jpg")
# 添加椒盐噪声，噪声比例 0.02
out = sp_noise(img, prob=0.02)

cv.imshow("img", out)
cv.waitKey()
