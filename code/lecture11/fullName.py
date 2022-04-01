# 测试函数
def get_full_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {last} {middle}"
    else:
        full_name = f"{first} {last}"
    return full_name

