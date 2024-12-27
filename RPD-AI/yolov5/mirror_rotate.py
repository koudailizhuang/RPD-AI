import os
import cv2
import numpy as np
from pathlib import Path


def flip_image_and_label(image_path, label_path, image_size):
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
    #flipped_image = cv2.flip(image, 1)  # 1表示水平翻转
    #图像旋转180度
    rotated_image = cv2.rotate(image,cv2.ROTATE_180)

    # 读取标签文件
    with open(label_path, 'r') as file:
        label_lines = file.readlines()

    # 更新标签中的坐标
    flipped_labels = []
    for line in label_lines:
        # 解析标签，YOLO格式：class_id x1 y1 x2 y2 ... xn yn
        parts = line.strip().split()
        class_id = int(parts[0])
        coordinates = [float(coord) for coord in parts[1:]]

        # 水平翻转时，所有的x坐标需要调整为 1 - x
        #flipped_coordinates = [1 - coordinates[i] if i % 2 == 0 else coordinates[i] for i in range(len(coordinates))]

        # 旋转 180° 时，所有的坐标需要调整
        # 对每个点的坐标进行变换 (x, y) -> (1 - x, 1 - y)
        rotated_coordinates = [1 - coordinates[i] if i % 2 == 0 else 1 - coordinates[i] for i in range(len(coordinates))]

        # 保存调整后的标签
        flipped_labels.append(f"{class_id} " + " ".join(map(str, rotated_coordinates)))

    # 返回翻转后的图像和更新后的标签
    return rotated_image, flipped_labels


def save_flipped_image_and_label(flipped_image, flipped_labels, save_image_path, save_label_path):
    """
    保存翻转后的图像和标签。

    :param flipped_image: 翻转后的图像
    :param flipped_labels: 翻转后的标签
    :param save_image_path: 保存翻转图像的路径
    :param save_label_path: 保存翻转标签的路径
    """
    # 保存翻转后的图像
    cv2.imwrite(save_image_path, flipped_image)

    # 保存翻转后的标签
    with open(save_label_path, 'w') as file:
        file.write("\n".join(flipped_labels))


def augment_dataset(image_dir, label_dir, output_dir):
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
            label_name = image_name.replace('.JPG', '.txt')  # 假设标签是.txt格式
            label_path = os.path.join(label_dir, label_name)

            # 图像大小（宽度和高度）
            image = cv2.imread(image_path)
            print(image_path)
            image_size = (image.shape[1], image.shape[0])  # (width, height)

            # 翻转图像和标签
            flipped_image, flipped_labels = flip_image_and_label(image_path, label_path, image_size)

            # 保存翻转后的图像和标签
            flipped_image_name = 'rotated_' + image_name
            flipped_label_name = 'rotated_' + label_name
            save_image_path = os.path.join(output_dir, flipped_image_name)
            save_label_path = os.path.join(output_dir, flipped_label_name)

            save_flipped_image_and_label(flipped_image, flipped_labels, save_image_path, save_label_path)

            print(f"Saved flipped images and labels for {image_name}")
        elif image_name.endswith('.jpg') :  # 只处理图像文件（假设是.jpg格式）
            # 图像和标签文件路径
            image_path = os.path.join(image_dir, image_name)
            label_name = image_name.replace('.jpg', '.txt')  # 假设标签是.txt格式
            label_path = os.path.join(label_dir, label_name)

            # 图像大小（宽度和高度）
            image = cv2.imread(image_path)
            print(image_path)
            image_size = (image.shape[1], image.shape[0])  # (width, height)

            # 翻转图像和标签
            flipped_image, flipped_labels = flip_image_and_label(image_path, label_path, image_size)

            # 保存翻转后的图像和标签
            flipped_image_name = 'rotated_' + image_name
            flipped_label_name = 'rotated_' + label_name
            save_image_path = os.path.join(output_dir, flipped_image_name)
            save_label_path = os.path.join(output_dir, flipped_label_name)

            save_flipped_image_and_label(flipped_image, flipped_labels, save_image_path, save_label_path)

            print(f"Saved flipped images and labels for {image_name}")



# 设置文件夹路径
image_dir = 'D:/algorithm/yolov5-v7.0-3/data/2024-12-all/images'  # 替换为图像文件夹路径
label_dir = 'D:/algorithm/yolov5-v7.0-3/data/2024-12-all/labels'  # 替换为标签文件夹路径
output_dir = 'D:/algorithm/yolov5-v7.0-3/data/2024-12-all/output'  # 替换为输出文件夹路径

# 创建输出文件夹（如果不存在）
Path(output_dir).mkdir(parents=True, exist_ok=True)

# 执行数据增强（镜像）
augment_dataset(image_dir, label_dir, output_dir)
