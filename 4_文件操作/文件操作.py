import os
import shutil

# os.getcwd()方法获取当前工作的目录current work directory
path = os.getcwd()
print(path)

# os.listdir()参数为目录字符串
print(os.listdir(path))

# Source path
src = path+"\\test.txt"

# Destination path
dst = path+"\\test_copy.txt"

# Destination2 path
dst2 = path+"\\移动文件\\test_move.txt"

FLAG = 2
if FLAG == 1:
    if os.path.isfile(src) == True:
        shutil.copy(src, dst)
elif FLAG == 2:
    if os.path.isfile(dst) == True:
        shutil.move(dst, dst2)
else:
    if os.path.isfile(dst2) == True:
        os.remove(dst2)
