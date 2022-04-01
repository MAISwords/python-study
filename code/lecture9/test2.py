# 使用类和实例

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


# 创建对象后修改属性的值
hero = Role('T.aoyan', 18, 20000, 10000, 5000, 3000, 99999)

print(hero.Name)
hero.HP = 90000
print(hero.HP)

# 修改攻击力
print(hero.ATK)
hero.updateAtk(9000)
print(hero.ATK)