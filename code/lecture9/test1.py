# 创建类

# 创建一个dog类  __init__()是一个特殊的函数，每次通过类创建对象时都会自动调用
# self这个形参必须要有
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} 现在坐下了！")

    def bark(self):
        print(f"{self.name} 在汪汪地叫！")

# 根据类创造实例
my_dog = Dog('simon', 3)
print(f"我的狗的名字叫做: {my_dog.name}")
print(f"我的狗今年 {my_dog.age} 岁了!")

# 调用方法
my_dog.sit()
my_dog.bark()