file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test8.txt","r")
file.seek(1,0)# 若文件内容为 ABCD, 则当前读写位置在 B.
char = file.read(2) # char得到 'BC' , file.read(1) 读取当前位置的2个字符
print(char)
file.close()