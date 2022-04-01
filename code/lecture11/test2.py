# 可通过的测试
# 导入单元测试模块
import unittest
# 导入要测试的函数
from fullName import get_full_name
# 创建一个类用于测试，并且继承unittest.TestCase
class NameTestCase1(unittest.TestCase):
    # 测试fullName.py

    def test(self):
        # 测试AAAA BBBB这样的姓名是否可行
        name1 = get_full_name('AAAA', 'BBBB')
        # 验证程序的结果是否与我们期望的结果相符合
        self.assertEqual(name1, 'AAAA BBBB')

    def test2(self):
        # 测试处理AAAA BBBB CCCC这样的姓名是否可行
        name2 = get_full_name('AAAA', 'BBBB', 'CCCC')
        self.assertEqual(name2,'AAAA BBBB CCCC')

# 开始点 执行程序时，所有以test打头的程序会自动运行
if __name__ == '__main__':
      unittest.main()