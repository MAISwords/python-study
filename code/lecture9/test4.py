# 导入类
# 从Cat.py文件中，导入其中的cat类
from Cat import cat
# 创建类和使用类
my_cat = cat('victory', 3)
my_cat.bark()

# 导入整个模块
import Dog
my_dog = Dog.dog('simon', 3)
my_dog.bark()

# 注意类和前面的函数一样，也可用as来指定别名
