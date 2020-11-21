# 追加模式打开文件,并不会同 “w“ 模式一样清空其中内容.
# 追加写入文件的内容，会被放到文件的末尾
file = open(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\6_读写文件内容\test5.txt","a")
file.write("123")
file.close()
