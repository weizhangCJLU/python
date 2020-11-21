file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\binary.bin",'rb')
# 让 file 将指定信息写入文件, file 一般不会马上写入.
char = file.read()
print(char)
file.close()