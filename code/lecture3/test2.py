# 修改列表元素
a = ['张三', '李四', '王五']
print(a)
a[0] = '赵六'
print(a)

# 添加列表元素，在列表尾部进行追加
b = ['张三', '李四', '王五']
print(b)
b.append('钱七')
print(b)

# 插入列表元素，在指定位置插入元素，后面的元素依次往后移动
c = ['张三', '李四', '王五']
print(c)
c.insert(1, '张五')
print(c)

# 删除列表元素
d = ['a', 'b', 'c', 'd', 'e']
print(d)
# 使用del删除,删除该元素，其他元素往前面移动
del d[1]
print(d)

# 使用pop()删除元素 从列表中删除后，该元素还能继续使用
e = ['a', 'b', 'c', 'd', 'e']
print(e)
a = e.pop()
print(e,a)

