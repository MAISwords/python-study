# 传递任意数量的实参
def making (*toppings):
    print(toppings)

making('a', 'b', 'c', 'd', 'e')
making('a', 'b', 'c')

# 例子 AOE范围伤害
def AOE (*targets):
    print("\n对以下目标造成500点伤害!")
    for i in targets:
        print(f"\t {i}")

AOE('张三', '李四', '王五')
AOE('赵六', '钱七')

# 使用任意数量的关键字实参
# **user_info表示创建一个名为user_info的字典
def build_info(first, last, **user_info):
    user_info['fistName'] = first
    user_info['lastName'] = last
    return user_info

user_profile = build_info('T.ao', 'yan', salary='50000')
print(user_profile)



