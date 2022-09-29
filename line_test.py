import cv2 as cv
import numpy as np
img = cv.imread(cv.samples.findFile('yhb1.jpg'))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,100,200,apertureSize = 3) #边缘100，200；钻孔分割 200，250
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=200,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    print(x1,y1,x2,y2)
cv.imwrite('houghlines5.jpg',img)