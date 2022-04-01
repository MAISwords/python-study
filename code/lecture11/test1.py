# 测试
from fullName import get_full_name
print("按下q键退出！")

# 测试循环
while True:
    first = input("\n请输入您的姓:")
    if first == 'q':
        break
    last = input("\n请输入您的名:")
    if first == 'q':
        break

    name = get_full_name(first, last)
    print(f"\n您的名字是:{name}")
