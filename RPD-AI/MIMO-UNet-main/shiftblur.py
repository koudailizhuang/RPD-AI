import cv2
import numpy as np


def tilt_shift_blur(image, start, end, blur_size):
    # 转换图像到HSV空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 创建一个掩膜，在指定区域之外是黑色
    mask = np.zeros_like(hsv[:, :, 1], dtype=np.uint8)
    mask[start[1]:end[1], start[0]:end[0]] = 255

    # 扩展掩膜以包括模糊区域
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (blur_size, blur_size))
    dilated_mask = cv2.dilate(mask, kernel, iterations=1)

    # 对HSV图像的饱和度通道应用模糊
    hsv[:, :, 1] = cv2.inpaint(hsv[:, :, 1], np.uint8(~dilated_mask), blur_size, cv2.INPAINT_TELEA)

    # 转换回BGR空间
    blurred_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # 混合原始图像和模糊图像
    result = cv2.addWeighted(image, 1, blurred_image, 0.5, 0)

    return result


# 读取图像
image = cv2.imread('C:/Users/djy/Desktop/5.JPG')

# 定义清晰区域的坐标
# (x_start, y_start) 是清晰区域的左上角坐标
# (x_end, y_end) 是清晰区域的右下角坐标
start = (100, 100)
end = (image.shape[1]-100, image.shape[0] - 100)

# 定义模糊大小
blur_size = 100

# 应用移轴模糊
blurred_image = tilt_shift_blur(image, start, end, blur_size)

# 保存结果
cv2.imwrite('C:/Users/djy/Desktop/6.JPG', blurred_image)