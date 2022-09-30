import cv2
import numpy as np
import sys
import time

from pyzbar import pyzbar
import decode_qrcode

# if len(sys.argv) > 1:
#     inputImage = cv2.imread(sys.argv[1])
# else:
inputImage = cv2.imread("qrcode_clip.jpg")


# 显示条码和二维码位置
def display(im, bbox):
	# bbox:Nx4x2
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[j][1]), (255, 0, 0), 1)
        cv2.line(im, tuple(bbox[j][1]), tuple(bbox[j][2]), (255, 0, 0), 1)
        cv2.line(im, tuple(bbox[j][2]), tuple(bbox[j][3]), (255, 0, 0), 1)
        cv2.line(im, tuple(bbox[j][3]), tuple(bbox[j][0]), (255, 0, 0), 1)

    # 显示
    cv2.imshow("Results", im)





# 创建一个 qrCodeDetector 对象
qrDecoder = cv2.QRCodeDetector()

# 检测和解码二维码
t = time.time()
data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)
print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))

height,width = inputImage.shape[:2]
#inputImage_resize = cv2.resize(inputImage,(width*4,height*4),interpolation=cv2.INTER_CUBIC)
result = decode_qrcode.get_qrcode_result(inputImage, binary_max=230, binary_step=2)
print(result)

if len(data) > 0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)
cv2.imwrite("output.jpg", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
