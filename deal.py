# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import os
import shutil

# 定义数据集路径
tiny_imagenet_dir = './tiny-imagenet-200'
output_dir = './data'

# 创建输出文件夹
os.makedirs(output_dir, exist_ok=True)

# 创建训练集文件夹
train_dir = os.path.join(output_dir, 'train')
os.makedirs(train_dir, exist_ok=True)

# 创建验证集文件夹
val_dir = os.path.join(output_dir, 'val')
os.makedirs(val_dir, exist_ok=True)

# 创建测试集文件夹
test_dir = os.path.join(output_dir, 'test')
os.makedirs(test_dir, exist_ok=True)

# 处理训练集图像和标签
train_data_dir = os.path.join(tiny_imagenet_dir, 'train')
train_labels_file = os.path.join(tiny_imagenet_dir, 'wnids.txt')

with open(train_labels_file, 'r') as f:
    for line in f:
        label = line.strip()
        label_dir = os.path.join(train_dir, label)
        os.makedirs(label_dir, exist_ok=True)
        label_data_dir = os.path.join(train_data_dir, label, 'images')
        for filename in os.listdir(label_data_dir):
            src = os.path.join(label_data_dir, filename)
            dst = os.path.join(label_dir, filename)
            shutil.copy(src, dst)

# 处理验证集图像和标签
val_data_dir = os.path.join(tiny_imagenet_dir, 'val')
val_labels_file = os.path.join(tiny_imagenet_dir, 'val/val_annotations.txt')

with open(val_labels_file, 'r') as f:
    for line in f:
        parts = line.split('\t')
        filename = parts[0]
        label = parts[1]
        label_dir = os.path.join(val_dir, label)
        os.makedirs(label_dir, exist_ok=True)
        src = os.path.join(val_data_dir, 'images', filename)
        dst = os.path.join(label_dir, filename)
        shutil.copy(src, dst)

# 处理测试集图像
test_data_dir = os.path.join(tiny_imagenet_dir, 'test', 'images')

for filename in os.listdir(test_data_dir):
    src = os.path.join(test_data_dir, filename)
    dst = os.path.join(test_dir, filename)
    shutil.copy(src, dst)

# 生成标签文件
labels_file = os.path.join(output_dir, 'labels.txt')

with open(labels_file, 'w') as f:
    # 处理训练集标签
    for label in os.listdir(train_dir):
        label_dir = os.path.join(train_dir, label)
        for filename in os.listdir(label_dir):
            f.write(f'{filename} {label}\n')

    # 处理验证集标签
    for label in os.listdir(val_dir):
        label_dir = os.path.join(val_dir, label)
        for filename in os.listdir(label_dir):
            f.write(f'{filename} {label}\n')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
