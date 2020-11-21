import shutil
import os

path = r'C:\Users\Lenovo\PycharmProjects\untitled1\project\7_文件自动归类\测试文件'
os.chdir(path)  # change directory切换当前工作目录
files = os.listdir(path)

for f in files:
    if os.path.isfile(f): # 判断是不是一个文件（文件夹，不处理）
        #folder_name = os.path.splitext(f)[-1][1:] + "文件夹"
        aa = os.path.splitext(f)
        cc = aa[-1][1:] # 从("abc", ".png" ) 获取"png"
        folder_name = cc + "文件夹"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            shutil.copy(f, folder_name)#shutil.move
        else:
            shutil.copy(f, folder_name)#shutil.move
