import numpy as np
import cv2 as cv

##qr_persective
##完成图片倾斜校正
##计算每个像素点mm尺寸 size_ratio
##引如wechat二维码识别

img = cv.imread('mid1.jpg',0)
#img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)




circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,50,
                            param1=210,param2=20,minRadius=5,maxRadius=20)
# HoughCircles(
#         InputArray image, //输入图像,必须是8位的单通道灰度图像
#         OutputArray circles, //输出结果，找到的圆信息
#         Int method, //方法是HOUGH_GRADIENT或HOUGH_GRADIENT_ALT
#         Double dp, //dp = 1或1.5
#         Double mindist, //最短距离-可以分辨是两个圆的，否则认为是同心圆
#         Double param1, //canny edge detection low threshold,Canny边缘检测的较大阈值
#         Double param2, //方法不同,含义不同
#
#         Int minradius, //最小半径
#         Int maxradius //最大半径

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # 绘制外圆
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # 绘制圆心
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    print("radis=",i[2])

cv.namedWindow('detected circles', cv.WINDOW_FREERATIO)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()