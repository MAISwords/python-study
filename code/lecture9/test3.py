# 继承
# 角色类
class Role:
    def __init__(self, Name, Age, HP, MP, ATK, DEF, Money):
        self.Name = Name
        self.Age = Age
        self.HP = HP
        self.MP = MP
        self.ATK = ATK
        self.DEF = DEF
        self.Money = Money

    def atkFunction(self):
        print(f"{self.Name} 发动攻击!")

    # 也可以通过在类中创造函数来对对象的值进行修改，这样做更安全
    def updateAtk(self, ATK):
        self.ATK = ATK

# 英雄类继承角色类
class Hero(Role):
    def __init__(self, Name, Age, HP, MP, ATK, DEF, Money):
        # 初始化父类属性
        super().__init__(Name, Age, HP, MP, ATK, DEF, Money)
    # 英雄类自己的函数
    def sp(self):
        print(f"\n我叫做{self.Name},我是一名英雄!")
    # 重写父类方法
    def atkFunction(self):
        print(f"{self.Name} 攻击一次！")

my_hero = Hero('T.aoyan', 18, 20000, 10000, 5000, 3000, 99999)
print(my_hero.Name)
# 调用父类函数
my_hero.atkFunction()
# 调用英雄类自己的函数
my_hero.sp()