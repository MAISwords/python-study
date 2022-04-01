# 使用setup()创建测试对象
# 测试类
# 导入测试模块
import unittest
# 导入类
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    # 针对AnonymousSurvey的测试

    def setUp(self):
        q = "你最喜欢的食物?"
        # 创建调查对象my_survey 和 答案仓库r
        self.my_survey = AnonymousSurvey(q)
        self.r = ['KFC', 'MDL', 'DKS']

    # 单例测试
    def test_store(self):
       self.my_survey.store_response(self.r[0])
       # 测试问题答案存进去了没
       self.assertIn(self.r[0], self.my_survey.responses)

    # 多例测试
    def test_store2(self):
        for i in self.r:
            self.my_survey.store_response(i)
        for i in self.r:
            self.assertIn(i, self.my_survey.responses)

# 开始点 优先执行setup()然后依次执行所有test
if __name__ == '__main__':
    unittest.main()