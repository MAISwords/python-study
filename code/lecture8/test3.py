# 传递列表
def greet_everone(names):
    for i in names:
        print(f"Hello, {i}")

userName = {'T.aoyan', '张三', '李四'}

greet_everone(userName)

# 在函数中修改列表 生产产品的例子
# 生产函数
def build_product(bluePrint, product):
    # pop()函数是从后往前面读所以要先倒置
    bluePrint.reverse()
    while bluePrint:
        a = bluePrint.pop()
        print(f"\n {a}已经生产出来了！")
        product.append(a)

# 打印产品函数
def print_product(product):
    for i in product:
        print(f"\n 生产出来的产品有{i}")

bP = ['a', 'b', 'c', 'd', 'e']
pd = []

build_product(bP, pd)
print_product(pd)

print(bP)
print(pd)

# 禁止函数中修改列表 生产产品的例子
def build_product1(bluePrint, product):
    # pop()函数是从后往前面读所以要先倒置
    bluePrint.reverse()
    while bluePrint:
        a = bluePrint.pop()
        print(f"\n {a}已经生产出来了！")
        product.append(a)

# 打印产品函数
def print_product1(product):
    for i in product:
        print(f"\n 生产出来的产品有{i}")

bP = ['a', 'b', 'c', 'd', 'e']
pd = []

# 在调用函数的时候，传递原列表的副本，可以避免原列表被修改
build_product(bP[:], pd)
print_product(pd)

print(bP)
print(pd)