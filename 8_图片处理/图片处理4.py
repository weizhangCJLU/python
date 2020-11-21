import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#设置所使用的字体
font = ImageFont.truetype("simfang.ttf", 50) # 仿宋字体

#打开图片
imageFile = r'C:\Users\Lenovo\PycharmProjects\untitled1\project\8_图片处理\2.jpg'
im1 = Image.open(imageFile)

#创建画图对象
draw = ImageDraw.Draw(im1)

# 设置文字 text()方法，参数为一个元组分别代表位置/内容/颜色/字体
# 位置以实际为准
draw.text((160, 0), "alex", (255, 0, 0), font=font)

#另存图片
im1.save("2_水印.jpg")
