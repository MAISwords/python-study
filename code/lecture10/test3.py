# 写入文件
# 程序会去寻找有没有save2.txt这个文件，如果没有的话，就创建一个
fileName = 'save2.txt'

# ’w‘是写入 ‘a’是附加模式，'r'是读取模式,'r+'读写模式
with open(fileName, 'w') as file_w:
    file_w.write("我在进行存档。。。。")

# 写入多行  每次写都会从头开始，把上一次的数据覆盖掉
with open(fileName,'w') as  file_w:
    file_w.write("我第二次进行存档！\n")
    file_w.write("我第三次进行存档！\n")