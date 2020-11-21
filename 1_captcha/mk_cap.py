#导入captcha包下的image文件中的ImageCaptcha类,使用之前先实例化
from captcha.image import ImageCaptcha
import random
import string

#characters为验证码上的字符集，10个数字加26个大写英文字母
#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ str类型
characters=string.digits+string.ascii_uppercase

x=170
y=80

#设置验证码图片的宽度widht和高度height
#除此之外还可以设置字体fonts和字体大小font_sizes
generator=ImageCaptcha(width=x,height=y)

#生成随机的4个字符的字符串
list=[random.choice(characters) for j in range(4)]
random_str=''.join(list)

#生成验证码
img=generator.generate_image(random_str)

#生成多张验证码
for i in range(10):
    generator=ImageCaptcha(width=x,height=y)
    random_str=''.join([random.choice(characters) for j in range(4)])
    img=generator.generate_image(random_str)

    file_name='C:/Users/Lenovo/PycharmProjects/untitled1/project/captcha/captcha_img/'+random_str+'_'+str(i)+'.jpg'
    img.save(file_name)
