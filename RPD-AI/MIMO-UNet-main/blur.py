import cv2
import numpy as np


def apply_variable_gaussian_blur(image, max_blur_radius):
    # 获取图像的高度和宽度
    height, width = image.shape[:2]

    # 创建一个用于存储结果的空白图像
    blurred_image = np.zeros_like(image)

    # 遍历图像的每一行
    for y in range(height):
        # 计算当前行的模糊半径，可以根据需要调整这个计算方式
        blur_radius = int(max_blur_radius * (y / (height - 1)))
        blur_radius = np.clip(blur_radius, 0, max_blur_radius)  # 确保半径在有效范围内

        # 如果模糊半径大于0，则对该行应用高斯模糊
        if blur_radius > 0:
            # 创建高斯模糊核
            blur_kernel_size = blur_radius * 2 + 1  # 高斯核大小应为奇数
            gaussian_blur_kernel = (blur_kernel_size, blur_kernel_size)

            # 应用高斯模糊
            blurred_row = cv2.GaussianBlur(image[y, :], gaussian_blur_kernel, 0)

            # 将模糊后的行复制回结果图像
            blurred_image[y, :] = blurred_row
        else:
            # 如果不需要模糊，则直接复制原图像的行
            blurred_image[y, :] = image[y, :]

    return blurred_image


# 读取图像
image = cv2.imread('C:/Users/djy/Desktop/5.JPG')

# 应用不同程度的高斯模糊
blurred_image = apply_variable_gaussian_blur(image, max_blur_radius=60)

# 显示处理后的图像
cv2.imshow('Variable Gaussian Blur', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()