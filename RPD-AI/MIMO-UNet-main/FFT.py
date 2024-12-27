import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
input_image_path = 'E:\SiAl\Camera MV-SUA33GM#0001-0003-Snapshot-20231116214835-5171190906301_2.JPG'
image = cv2.imread(input_image_path)

# 将图像从BGR转换为RGB（如果需要的话）
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 对每个颜色通道进行傅里叶变换
fourier_transforms = []
for channel in cv2.split(image):
    # 应用傅里叶变换
    f = np.fft.fft2(channel)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    fourier_transforms.append(magnitude_spectrum)

# 显示原始图像和频率谱
plt.figure(figsize=(12, 6))

# 显示原始图像
plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# 显示每个通道的频率谱
for i, transform in enumerate(fourier_transforms, start=2):
    plt.subplot(1, 4, i)
    plt.imshow(transform, cmap='gray')
    plt.title(f'Frequency Spectrum of Channel {i - 1}')
    plt.axis('off')

plt.show()