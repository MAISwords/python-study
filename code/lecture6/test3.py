# 遍历字典
staff = {'name':'T.aoyan', 'age':'26', 'salary':'15000'}
# i和j分别表示键和值
for i, j in staff.items():
    print(i)
    print(j)

# 优化打印结果
for i, j in staff.items():
    print(f"staff's {i} is {j}")