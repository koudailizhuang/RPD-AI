import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def blur_image(path, savepath):
    for file in os.listdir(path):
        if file.endswith(".JPG"):
            path_name = savepath+"/"+file
            image = cv2.imread(path+"/"+file)

            # 转换为RGB颜色空间（OpenCV默认为BGR）
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 获取图像的高度和宽度
            height, width, _ = image_rgb.shape

            # 创建一个用于存储结果的空白图像
            result = np.zeros_like(image_rgb)

            # 设定清晰区域的位置（可以根据需求调整）
            clear_height_range = (300, height // 5)  # 中间区域保持清晰

            # 遍历每一行，逐行应用模糊效果
            for y in range(height):
                # 计算模糊强度，距离中心越远，模糊越强
                if clear_height_range[0] <= y <= clear_height_range[1]:
                    result[y] = image_rgb[y]  # 中心区域保持清晰
                else:
                    # 以中心区域的y值为基准，计算每个像素的模糊程度
                    blur_strength = int(abs(y - height // 2) // 10) * 2 + 21  # 模糊强度逐渐增加
                    blurred_row = cv2.GaussianBlur(image_rgb[y:y + 1], (blur_strength, blur_strength), 0)
                    result[y] = blurred_row[0]  # 将模糊的行放入结果图像
            cv2.imwrite(path_name, result)

path = 'D:/algorithm/datasets/SiAl/out2_mirror'
savepath = 'D:/algorithm/datasets/SiAl/out2_mirror_blur'

blur_image(path, savepath)

