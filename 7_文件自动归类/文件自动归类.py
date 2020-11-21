import os

del_dir = r"C:\Users\Lenovo\PycharmProjects\untitled1\project\7_文件自动归类\测试文件"

fileList = os.listdir(del_dir)

# 将 fileList里面的元素，逐一放到f里，再对f进行操作
for f in fileList:
# 不用[1]，防止文件没有后缀名例如：aa拆分后也只有1个元素（aa），想要取【1】就越界了
    if os.path.splitext(f)[-1] == ".jpg":
        print(f)
