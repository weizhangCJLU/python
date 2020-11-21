file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test6.txt","r")
line = file.readline()
# 我们一般不知道一个文件中有多少行.
# readline 在读取到文件末尾的时候会返回一个空字符串,
# 我们可以以此来判断是否已经读取了所有行.
while line != "":
  print(line)
  line = file.readline()
file.close()
