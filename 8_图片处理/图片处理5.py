from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open(r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2.jpg')
img_size = im.size

# 把图片平均分成9块
w = img_size[0] / 2.0
h = img_size[1] / 2.0
x = 0
y = 0

for i in range(2):
    for j in range(2):
        img1 = im.crop((x, y, x + w, y + h))
        img1.save("crop_{}{}.jpg".format(i, j))
        x += w
    x=0
    y += h
