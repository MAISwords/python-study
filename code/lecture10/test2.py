# 使用文件
fileName = 'save.txt'

with open(fileName) as file_1:
    a = file_1.read()

p_string = ''
for i in a:
    p_string += i.rstrip()

print(p_string)

