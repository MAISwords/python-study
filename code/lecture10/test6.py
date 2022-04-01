# 文件异常
# fileName = 'a.txt'
#
# try:
#     with open(fileName, encoding='utf-8') as f:
#         a = f.read()
# except FileNotFoundError:
#     print(f"文件{fileName}不存在!")

# 例子统计多个文件中字符长度
def count_file (filename):
    try:
        with open(filename) as f1:
            b = f1.read()
    except FileNotFoundError:
        print(f"文件{filename}不存在!")
    else:
        l = len(b)
        print(f"文件{filename}有{l}个字符!")

f = ['save.txt', 'save1.txt', 'save2.txt', 'save3.txt']
for i in f:
    count_file(i)