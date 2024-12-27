import os
import cv2
import numpy as np
from pathlib import Path


def flip_image_and_label(image_path):
    """
    对图像和标签进行水平翻转，并调整标签坐标。

    :param image_path: 图像文件路径
    :param label_path: 标签文件路径 (YOLO格式 .txt)
    :param image_size: 图像的尺寸 (width, height)
    :return: 翻转后的图像和更新后的标签内容
    """
    # 读取图像
    image = cv2.imread(image_path)

    # 获取图像的宽度和高度
    height, width, _ = image.shape

    # 图像水平翻转
    flipped_image = cv2.flip(image, 1)  # 1表示水平翻转
    #图像旋转180度
    #rotated_image = cv2.rotate(image,cv2.ROTATE_180)

    # 返回翻转后的图像和更新后的标签
    return flipped_image


def save_flipped_image_and_label(flipped_image, save_image_path):
    """
    保存翻转后的图像和标签。

    :param flipped_image: 翻转后的图像
    :param flipped_labels: 翻转后的标签
    :param save_image_path: 保存翻转图像的路径
    :param save_label_path: 保存翻转标签的路径
    """
    # 保存翻转后的图像
    cv2.imwrite(save_image_path, flipped_image)



def augment_dataset(image_dir, output_dir):
    """
    对数据集进行镜像增强。

    :param image_dir: 图像所在文件夹路径
    :param label_dir: 标签所在文件夹路径
    :param output_dir: 输出增强后图像和标签的文件夹路径
    """
    # 遍历图像文件夹
    for image_name in os.listdir(image_dir):
        print(image_name)
        if image_name.endswith('.JPG') :  # 只处理图像文件（假设是.jpg格式）
            # 图像和标签文件路径
            image_path = os.path.join(image_dir, image_name)

            # 图像大小（宽度和高度）
            image = cv2.imread(image_path)
            #print(image_path)
            image_size = (image.shape[1], image.shape[0])  # (width, height)

            # 翻转图像和标签
            flipped_image = flip_image_and_label(image_path)

            # 保存翻转后的图像和标签
            flipped_image_name = 'rotated_' + image_name
            save_image_path = os.path.join(output_dir, flipped_image_name)

            save_flipped_image_and_label(flipped_image, save_image_path)

            print(f"Saved flipped images and labels for {image_name}")
        elif image_name.endswith('.JPG'):  # 只处理图像文件（假设是.jpg格式）
            # 图像和标签文件路径
            image_path = os.path.join(image_dir, image_name)

            # 图像大小（宽度和高度）
            image = cv2.imread(image_path)
            # print(image_path)
            image_size = (image.shape[1], image.shape[0])  # (width, height)

            # 翻转图像和标签
            flipped_image = flip_image_and_label(image_path)

            # 保存翻转后的图像和标签
            flipped_image_name = 'rotated_' + image_name
            save_image_path = os.path.join(output_dir, flipped_image_name)

            save_flipped_image_and_label(flipped_image, save_image_path)

            print(f"Saved flipped images and labels for {image_name}")



# 设置文件夹路径
image_dir = 'D:/algorithm/datasets/SiAl/out2'  # 替换为图像文件夹路径
output_dir = 'D:/algorithm/datasets/SiAl/out2_mirror'  # 替换为输出文件夹路径

# 创建输出文件夹（如果不存在）
Path(output_dir).mkdir(parents=True, exist_ok=True)

# 执行数据增强（镜像）
augment_dataset(image_dir, output_dir)
