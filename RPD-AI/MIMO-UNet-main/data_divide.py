import os
import shutil
import random

# 设置原始数据集文件夹和目标文件夹路径
source_images_folder = 'path/to/your/images'  # 原始图像文件夹路径
source_labels_folder = 'path/to/your/labels'  # 原始标签文件夹路径
train_images_folder = 'path/to/your/train/images'  # 训练集图像文件夹路径
val_images_folder = 'path/to/your/val/images'  # 验证集图像文件夹路径
train_labels_folder = 'path/to/your/train/labels'  # 训练集标签文件夹路径
val_labels_folder = 'path/to/your/val/labels'  # 验证集标签文件夹路径

# 创建训练集和验证集的文件夹，如果不存在的话
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(val_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(val_labels_folder, exist_ok=True)

# 获取源图像文件和标签文件
image_files = [f for f in os.listdir(source_images_folder) if f.endswith(('jpg', 'png', 'jpeg'))]
label_files = [f for f in os.listdir(source_labels_folder) if f.endswith('.txt')]

# 确保图像和标签文件一一对应
assert len(image_files) == len(label_files), "The number of images and labels do not match."

# 按 4:1 的比例划分数据集
num_files = len(image_files)
train_size = int(num_files * 0.8)  # 80% 作为训练集
val_size = num_files - train_size  # 20% 作为验证集

# 随机打乱文件列表
random.seed(42)  # 设置随机种子，确保可重复性
random.shuffle(image_files)

# 划分训练集和验证集
train_images = image_files[:train_size]
val_images = image_files[train_size:]

# 复制图像和标签到训练集和验证集文件夹
for img_file in train_images:
    # 图像文件路径
    img_path = os.path.join(source_images_folder, img_file)
    label_path = os.path.join(source_labels_folder,
                              img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))

    # 复制到训练集文件夹
    shutil.copy(img_path, os.path.join(train_images_folder, img_file))
    shutil.copy(label_path, os.path.join(train_labels_folder,
                                         img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg',
                                                                                                          '.txt')))

for img_file in val_images:
    # 图像文件路径
    img_path = os.path.join(source_images_folder, img_file)
    label_path = os.path.join(source_labels_folder,
                              img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))

    # 复制到验证集文件夹
    shutil.copy(img_path, os.path.join(val_images_folder, img_file))
    shutil.copy(label_path, os.path.join(val_labels_folder,
                                         img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg',
                                                                                                          '.txt')))

print(f"Dataset split complete. {train_size} images in the train set, {val_size} images in the validation set.")
