# 读取文档案例1
# 在与test1.py同目录文件夹下面查找save.txt文件

with open('save.txt') as file_object:
    a = file_object.read()

print(a)
# 用于删除后面的空格
print(a.rstrip())