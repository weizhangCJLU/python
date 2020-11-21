# “w” 模式在写入已经存在的文本文件时会将其中的内容全部清空,再写入
# 指定内容
file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test2.txt",'w')
file.write("123")  # 擦除文件所有内容，再写入
file.close()
