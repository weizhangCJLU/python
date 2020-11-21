import os
import shutil

# os.getcwd()方法获取当前工作的目录current work directory
path = os.getcwd()
print(path)

src = path+"\\Lema"
dst = path+"\\Lema_copy"
dst2 = path+"\\Lema_copy2"

FLAG = 4
if FLAG == 1:
    if os.path.isdir(src) == False:
        os.mkdir(src)  # 创建一个文件夹Lema
elif FLAG == 2:
    if os.path.isdir(src) == True:
        shutil.copytree(src, dst)  # 复制文件夹Lema，并重命名为Lema_copy
elif FLAG == 3:
    if os.path.isdir(dst) == True:
        os.rename(dst,dst2) #将文件夹Lema_copy重命名为Lema_copy2
else:
    if os.path.isdir(dst2) == True:
        shutil.rmtree(dst2) #删除文件夹Lema_copy2
