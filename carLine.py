import numpy as np
import cv2
import math

src = cv2.imread("C:/Users/yuido/cv/202178009_kimyeju/lane.jfif", 1)

if src is None:
    print('Image load failed!')
    exit()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 200, 255)# 198, 230)150,200
cv2.imshow('edge', edge)
cv2.waitKey(0)
lines = cv2.HoughLines(edge, 1, (math.pi / 180),90)#min_theta = 10, max_theta=180, 개수:260,90

dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)


line1=[]
line2=[]
if lines is not None:
    for i in range(lines.shape[0]):
        rho = lines[i][0][0] #rho
        theta = lines[i][0][1] #theta
        print(theta*180/math.pi)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        x0, y0 = rho * cos_t, rho * sin_t
        
        alpha = 1000
        pt1 = (int(x0 - alpha * sin_t), int(y0 + alpha * cos_t))
        pt2 = (int(x0 + alpha * sin_t), int(y0 - alpha * cos_t))

        if theta*180/math.pi < 47:#50
            line1.append([theta,pt1,pt2])
            cv2.line(dst, pt1, pt2, (0, 0, 255), 1, cv2.LINE_AA)
           
        elif theta*180/math.pi > 135:#120
            line2.append([theta,pt1,pt2])
            cv2.line(dst, pt1, pt2, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()
line1.sort()
line2.sort()
idx1 = len(line1)//2
idx2 = len(line2)//2

cv2.line(src, line1[idx1][1],line1[idx1][2], (0, 0, 255), 1, cv2.LINE_AA)
cv2.line(src, line2[idx2][1],line2[idx2][2], (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow('src', src)
cv2.waitKey(0)
cv2.imwrite("C:/Users/yuido/cv/202178009_kimyeju/houghline_lane.jfjf", src)
cv2.destroyAllWindows()
