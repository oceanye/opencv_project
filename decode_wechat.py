import time
import cv2
import numpy as np

inputImage = cv2.imread("qrcode_clip.jpg")

WechatQRmodel = cv2.wechat_qrcode_WeChatQRCode('detect.prototxt', 'detect.caffemodel', 'sr.prototxt', 'sr.caffemodel')
start = time.time()
codeinfo, pts = WechatQRmodel.detectAndDecode(inputImage)
end = time.time()
print(codeinfo, pts)
print('time usage: ', end - start)
cv2.drawContours(inputImage, [np.int32(pts)], -1, (0, 0, 255), 2)
cv2.imshow('QR', inputImage)
cv2.waitKey(0)
# ['Hello :)'] [array([[ 43.84111 ,  32.450653],
#       [211.51726 ,  32.450653],
#       [211.51726 , 222.97139 ],
#       [ 43.84111 , 222.97139 ]], dtype=float32)]
#time usage:  0.027999401092529297
