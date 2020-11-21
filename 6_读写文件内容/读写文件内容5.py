# ‘w+’ 模式打开文件,既可以读取文件,也可以写入文件,不过写入文件的方式
# 是先将文件中的内容全部清空,然后把程序指定的数据写
file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test4.txt",'w+')
file.write("123")
file_content = file.read()
file.close()
print(file_content)
