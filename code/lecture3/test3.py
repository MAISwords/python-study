# 列表排序 会改变a的序列
a = [4, 3, 2, 15, 4, 54, 3, 23, 4]
print(a)
# 从小到大排序
a.sort()
print(a)
# 倒置
a.reverse()
print(a)

# 临时排序 不会改变b的序列
b = [4, 3, 2, 15, 4, 54, 3, 23, 4]
print(b)
print(sorted(b))
print(b)

# 求长度
print(len(b))