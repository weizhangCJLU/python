file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test3.txt",'r+')
file.write("123")
# 将光标后面的内容读取出来
file_content = file.read()
file.close()
print(file_content)