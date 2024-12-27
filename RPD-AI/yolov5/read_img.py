import os
import cv2
import numpy as np
import math
path='D:/algorithm/yolov5-v7.0-3/data/5_1.JPG'
filepath='D:/algorithm/yolov5-v7.0-3/data/5_6.JPG'
img = cv2.imread(path)
img1=img*1.1
(B,G,R)=cv2.split(img)

cv2.imwrite(filepath, img1)  # 将生成图片a存入路径。