# 以“只读模式”获取指定文件的操作信息放入 file 变量, 之后将可以通过
# file 对指定的文件进行操作.
f = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test.txt", 'r')
# 将 file 对应的文件的全部内容读入 file_content
file_content = f.read()
# 将文件关闭, 否则文件将处于被引用状态,若该文件位于 u 盘,则 u 盘是无法
# 正常弹出的
f.close()
print(file_content)
