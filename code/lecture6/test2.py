# 使用字典
staff = {'name':'T.aoyan', 'age':'26', 'salary':'15000'}

# 访问字典中的值
a = staff['name']
print(f"指挥官的姓名是:{a}，是一位领导！")

# 添加键值对
staff['HP'] = 999999
staff['MP'] = 999999
print(staff)

# 修改字典中的值  在游戏开发过程中，可以用来修改角色每次移动的坐标
staff['salary'] = 999999
print(staff)

# 删除键值对
del staff['salary']
print(staff)

# 使用get()函数来访问字典，这样一来，如果字典中没有这个键，程序不会报错
a = staff.get('salary','没有这个数据！')
print(a)