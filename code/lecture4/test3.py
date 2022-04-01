# 使用列表一部分
zimu = ['a', 'b', 'c', 'd', 'e']

# 打印3个元素，从下标0开始，到3的前一个索引为止
print(zimu[0:3])

# 遍历前三个元素
for i in zimu[:3]:
    print(i)

# 遍历后三个元素
for i in zimu[-3:]:
    print(i)

# 复制列表
zimu = ['a', 'b', 'c', 'd', 'e']
zimu1 = zimu[1:3]
print(zimu1)