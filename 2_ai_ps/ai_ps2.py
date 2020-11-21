import os
import shutil
import removebg
# 根据apikey 创建一个remove background 对象
rmbg = removebg.RemoveBg("2FPyYH9eRvs5T6Vh8Wqf7gmL","error.log")

# 把这个文件夹下的图片，批量抠图
del_dir = r"C:\Users\Lenovo\PycharmProjects\untitled1\project\ai_ps\raw_img"

# 扣好的图片，放到这个文件夹下
new_folder = os.path.join(del_dir, "无背景文件夹")

# 批量去除背景
def batch_removebg():
    fileList = os.listdir(del_dir)
    for f in fileList:
        # -1，避免splitext("tank")==>["tank"]
        suffix = os.path.splitext(f)[-1]   # 获取文件后缀
        if suffix == ".png" or suffix == ".jpg":  # 如果后缀是 .png 或 .jpg
            rmbg.remove_background_from_img_file(os.path.join(del_dir,f))

# 创建一个新的文件夹，存储新图片
def make_new_folder():
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

# 把新图片，都放到一个新的文件夹
def copy_new_pic():
    fileList = os.listdir(del_dir)
    for f in fileList:
        if f.count("no_bg") > 0: # 如果文件名包含no_bg就是刚刚去除背景的图片
            shutil.move(os.path.join(del_dir,f), new_folder)

# 执行程序
make_new_folder()
batch_removebg()
copy_new_pic()
