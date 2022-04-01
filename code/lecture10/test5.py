# 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("你不能用一个数除以0!")

# 例子一个除法程序，用户输入为q时退出程序

while True:
    num1 = input("\n请输入被除数:")
    if num1 == 'q':
        break
    num2 = input("\n请输入除数:")
    if num2 == 'q':
        break
    # 对0进行检测
    try:
      answer = int(num1) / int(num2)
    except ZeroDivisionError:
       print("你不能用一个数除以0!")
    else:
        print(answer)