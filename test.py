# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import torchvision
import torchvision.models as models
import torch
from PIL import Image

# 读取图像f
# 数据预处理

# 缩放
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])])

# 根据保存方式加载
# 加载预训练的ResNet-18模型
model = models.resnet18()
# 获取模型的最后一层全连接层
num_features = model.fc.in_features

# 替换最后一层全连接层并设置输出维度为num_classes
num_classes = 200
model.fc = torch.nn.Linear(num_features, num_classes)

# 初始化新的全连接层的权重
torch.nn.init.zeros_(model.fc.bias)
model.load_state_dict(torch.load('model_best.pth.tar')['state_dict'])

model2 = models.resnet18()
# 获取模型的最后一层全连接层
num_features = model2.fc.in_features

# 替换最后一层全连接层并设置输出维度为num_classes
num_classes = 200
model2.fc = torch.nn.Linear(num_features, num_classes)

# 初始化新的全连接层的权重
torch.nn.init.zeros_(model2.fc.bias)
model2.load_state_dict(torch.load('checkpoint.pth.tar')['state_dict'])
# 注意维度转换，单张图片

dif = []
# 测试开关
model.eval()
model2.eval()
# 节约性能
m = 0
k = 0
for i in range(10000):
    try:
        img = Image.open("./images/test_" + str(i) + ".JPEG")
        image = transform(img)
        image1 = image
        image1 = image.unsqueeze(0)
        with torch.no_grad():
            output = model(image1)
            output2 = model2(image1)
    # print(output.argmax(1))
    # 定义类别对应字典
    # 转numpy格式,列表内取第一个
        a = output.argmax(1).numpy()[0]
        b = output2.argmax(1).numpy()[0]
        if a == b:
            k += 1
        else:
            dif.append('test_' + str(i) + ".JPEG")
        print("test_" + str(i) + ':')
        print("output1 :", a)
        print('output2 :', b)
        m+=1
    except:
        continue



    # img.show()
    # top_k = torch.topk(output, k=5)
    # top_indices = top_k.indices[0]
    # top_values = top_k.values[0]

    # print("Top 5 Indices:", top_indices)
    # print("Top 5 Values:", top_values)
print('相似率 :', k / m)
print('判断结果不同的图片：')
print(dif)
