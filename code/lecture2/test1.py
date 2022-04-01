# 第一个python程序
print("Hello Python!")

# 字符串例子
first_name = "Tao"
last_name = "Yan"
# 这里的f起到一个合并的作用
full_name = f"{first_name} {last_name}"
hello = f"Hello, {full_name}!"
print(full_name)
print(hello)

# 去掉字符串前后空白
name = " TaoYan "
a = name.lstrip()
a = a.strip()
print(a)