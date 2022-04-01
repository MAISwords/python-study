# 导入模块的全部函数
import addFunction

# 导入模块的部分函数
from minusFunction import minus

# 导入模块的部分函数并起别名
from minusFunction import minus_100 as m1

#导入模块的全部函数调用法
c = addFunction.add(1, 2)
print(c)

#导入模块的部分函数调用法
d = minus(10, 2)
print(d)

# 用as给其他模块的函数起别名
e = m1(1)
print(e)
