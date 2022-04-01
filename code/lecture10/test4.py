# 附加到文件
fileName = 'save3.txt'
# 写入多行  每次写都会从头开始，把上一次的数据覆盖掉
with open(fileName,'w') as  file_w:
    file_w.write("我第二次进行存档！\n")
    file_w.write("我第三次进行存档！\n")

with open(fileName,'a') as  file_w:
    file_w.write("我第四次进行存档！\n")
    file_w.write("我第五次进行存档！\n")