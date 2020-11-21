# w模式，如果not_exist.txt文件不存在，就会自动创建一个文件
f = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\not_exist.txt",'w')
# 让 file 将指定信息写入文件, file 一般不会马上写入.
f.write("Hello 空文件")
# 写入文件的信息,一般先保存在内存之中,关闭之后,会将内存中的数据写入文件
f.close()
