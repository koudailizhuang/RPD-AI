'''
机器学习中随机产生负样本的
'''
import os
import cv2
import random

# 读取图片
#img = cv2.imread('E:/2023-11-16/Camera MV-SUA33GM#0001-0003-Snapshot-20231116215125-5172892872562.JPG')

img_dir = 'E:/SiAl/add'
img_out_dir = 'E:/SiAl/out1'
files = os.listdir(img_dir)

for file in files :
    img = cv2.imread(img_dir+'/'+file)
    h = 300
    w = 200

    count = 1
    while 1:
        # 随机产生x,y   此为像素内范围产生
        y = random.randint(0, 340)
        x = random.randint(0, 320)
        # 随机截图
        # cropImg = img[(y):(y + h), (x):(x + w)]
        cropImg = img[120:420, (y):(y + h)]
        cv2.imwrite(img_out_dir+'/'+file[:-4]+'_'+ str(
            count) + '.JPG', cropImg)
        count += 1

        if count == 10:
            break

'''
# h、w为想要截取的图片大小
h = 200
w = 200

count = 1
while 1:
    # 随机产生x,y   此为像素内范围产生
    y = random.randint(0, 392)
    x = random.randint(0, 320)
    # 随机截图
    #cropImg = img[(y):(y + h), (x):(x + w)]
    cropImg = img[130:330,(y):(y+h)]
    cv2.imwrite('E:/2023-11-16-cut/Camera MV-SUA33GM#0001-0003-Snapshot-20231116215125-5172892872562_' + str(count) + '.JPG', cropImg)
    count += 1

    if count == 20:
        break
'''