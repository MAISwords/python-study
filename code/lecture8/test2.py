# 返回值

def add_function(num1, num2):
    return num1 + num2

a = 3
b = 5
c = add_function(a, b)
print(c)

# 返回字典  在游戏中可以用于创造角色使用
def build_role(role_name, role_grade):
    role = {
        'NAME':role_name,
        'GRADE':role_grade,
        'HP':4000,
        'MP':2000,
        'ATK':1200,
        'DEF':300
    }
    return role

a = build_role('T.aoyan', 3)
print(a)
