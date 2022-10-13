import cv2 as cv
import numpy as np
import math
def line_angle(x1,y1,x2,y2):
    theta = math.atan((y2-y1)/(x2-x1))/math.pi*180
    #print(theta)
    return theta
def line_length(x1,y1,x2,y2):
    length = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return length

import numpy as np

def point_distance_line(point,line_point1,line_point2): #line_point = np.array([xi,yi])
	#计算向量
    vec1 = line_point1 - point
    vec2 = line_point2 - point
    distance = np.abs(np.cross(vec1,vec2)) / np.linalg.norm(line_point1-line_point2)
    return distance


## 获取直线 与 点的垂足
def get_foot(start_point, end_point, point_a):
    start_x, start_y = start_point
    end_x, end_y = end_point
    pa_x, pa_y = point_a

    p_foot = [0, 0]
    if start_point[0] == end_point[0]:
        p_foot[0] = start_point[0]
        p_foot[1] = point_a[1]
        return p_foot

    k = (end_y - start_y) * 1.0 / (end_x - start_x)
    a = k
    b = -1.0
    c = start_y - k * start_x
    p_foot[0] = int((b * b * pa_x - a * b * pa_y - a * c) / (a * a + b * b))
    p_foot[1] = int((a * a * pa_y - a * b * pa_x - b * c) / (a * a + b * b))

    return p_foot


#point = np.array([(x1+x2)/2,(y1+y2)/2])
#line_point1 = np.array([xi,yi])
#line_point2 = np.array([xj,yj])




img = cv.imread(cv.samples.findFile('yhb1.jpg'))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,100,200,apertureSize = 3) #边缘100，200；钻孔分割 200，250
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=80,maxLineGap=10)

lines2=[]

for line in lines:
    x1,y1,x2,y2 = line[0]
    angle = line_angle(x1,y1,x2,y2)
    aim_angle = -45
    if abs(angle-aim_angle)<20: # 筛选特定角度的线段
        cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        lines2.append(line)



for line in lines2:




    x1, y1, x2, y2 = line[0]

    for line1 in lines2:
        xi,yi,xj,yj=line1[0]
        xm,ym = int((x1 + x2) / 2), int((y1 + y2) / 2)

        len1 = line_length(x1, y1, x2, y2)
        len2 = line_length(xi,yi,xj,yj)
        if len1<len2:
            p_foot=get_foot((xi,yi),(xj,yj),(xm,ym))
            cv.line(img,p_foot,(xm,ym),(255,0,0),2)
            d=line_length(xm,ym,p_foot[0],p_foot[1])
            cv.putText(img, 'dist=' + str(round(d)), (int((xm + p_foot[0]) / 2), int((ym + p_foot[1]) / 2)),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    length = line_length(x1, y1, x2, y2)
    cv.putText(img, str(round(angle)) + ',' + str(round(length)), (int((x1 + x2) / 2), int((y1 + y2) / 2)),
               cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    print('(', x1, ',', y1, ');(', x2, ',', y2, ')')

cv.imwrite('houghlines5.jpg',img)