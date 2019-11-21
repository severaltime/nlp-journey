import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import resnet50

# 加载 Keras训练好的ResNet50模型
model = resnet50.ResNet50()

# 加载图片, 调整格式大小为：224x224像素
img = image.load_img("./dataset/bay.jpg", target_size=(224, 224))

# 把图片转为numpy数组
x = image.img_to_array(img)

# keras预测的是多张图片列表，所以多加一个维度
x = np.expand_dims(x, axis=0)

# 数据归一化：resnet50模型
x = resnet50.preprocess_input(x)

# 开始预测
predictions = model.predict(x)

# 查看图像的label
predicted_classes = resnet50.decode_predictions(predictions, top=9)

print("This is an image of:")

for imagenet_id, name, likelihood in predicted_classes[0]:
    print(" - {}: {:2f} likelihood".format(name, likelihood))

