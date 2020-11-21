from PIL import Image

im1 = Image.open(r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2.jpg')
print(im1.size)

# crop()方法，作用裁剪图片，参数是一个列表或元组，其中前两个为起点x,y
# 后两个参数为终点x,y
# 对图片仅需两个点就可以确定大小
# 教师演示一个点固定，拖动其他任意一个改变图片大小，位置以实际为准
#box = [0, 0, 150, 205]
box = [150, 205, 300, 410]
im_crop = im1.crop(box)
im_crop.save("2_裁剪.jpg")
