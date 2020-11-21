from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open(r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2.jpg')

# rotate()函数，作用旋转图片，参数为Int，代表角度值
im.rotate(45).save('rotate45.png') # 逆时针旋转
im.rotate(90).save('rotate90.png')
im.rotate(180).save('rotate180.png')
im.rotate(-45).save('rotate-45.png')
im.rotate(-90).save('rotate-90.png')

# transpose()函数，作用图片转换，有多种模式，这里使用翻转模式flip
im.transpose(Image.FLIP_LEFT_RIGHT).save('左右翻转.png')
im.transpose(Image.FLIP_TOP_BOTTOM).save('上下翻转.png')
