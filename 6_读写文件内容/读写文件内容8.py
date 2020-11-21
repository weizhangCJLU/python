file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test7.txt","r")
# all_lines 是一个列表,列表中每一项都是文件中的一行
all_lines = file.readlines()
print(all_lines)
