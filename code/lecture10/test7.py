# 存储数据
# 导入模块
import json
# 定义一个数字列表
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 定义要存入的文件名
fileName = 'num.json'

# 写
with open(fileName, 'w') as f:
    # 将列表num放入f中，以json格式存储
    json.dump(num, f)

# 读
with open(fileName) as f1:
    a = json.load(f1)

print(a)