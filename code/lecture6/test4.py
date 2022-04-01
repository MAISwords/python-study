# 字典嵌套
staff1 = {'name':'T.aoyan', 'age':'26', 'salary':'15000'}
staff2 = {'name':'张三', 'age':'20', 'salary':'10000'}
staff3 = {'name':'李四', 'age':'18', 'salary':'8000'}
# 字典列表
staffs = [staff1, staff2, staff3]
for i in staffs:
    print(i)

# 实例
enemy = []
# 创建30个敌人
for new_enemy in range(30):
    new_enemy = {'HP':'1000', 'ATK':'200', 'DEF':'100'}
    enemy.append(new_enemy)

print(enemy)

# 其中前5个敌人为小BOSS
for new_enemy in enemy[:5]:
    new_enemy['HP'] = 4000
    new_enemy['ATK'] = 500
    new_enemy['DEF'] = 300

print(enemy)

# 字典中嵌套列表 例子遍历BOSS攻击方式
boss = {'HP':'20000', 'ATK':'2000', '攻击方式':['火球攻击', '闪电攻击', '防守反击', '换血大法']}

for i in boss['攻击方式']:
    print(i)

# 字典中嵌套字典 例子多个游戏玩家登录
users = {
    'T.aoyan':{'name':'T.aoyan','HP':'99999', 'ATK':'99999'},
    '李四':{'name':'李四','HP':'2000', 'ATK':'200'},
    '张三':{'name':'张三','HP':'3000', 'ATK':'300'},

}

for i, j in users.items():
    print(f"{i}的生命值是:{j['HP']},  攻击力是:{j['ATK']}！")

