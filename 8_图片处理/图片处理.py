from PIL import Image

im = Image.open(r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2.jpg') # 图片名字按实际替换

w, h = im.size
print('图像尺寸: {} * {}'.format(w, h))

im.thumbnail((w//2, h//2))
w, h = im.size
print('图像缩放后尺寸: {} * {}'.format(w, h))
#im.show()
im.save(r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2_缩放.jpg')