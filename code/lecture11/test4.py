# 测试类
# 导入测试模块
import unittest
# 导入类
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    # 针对AnonymousSurvey的测试
    # 单例测试
    def test_store(self):
        q = "你最喜欢的食物?"
        my_s = AnonymousSurvey(q)
        my_s.store_response('KFC')
        # 测试问题答案存进去了没
        self.assertIn('KFC', my_s.responses)

    # 多例测试
    def test_store2(self):
        q = "你最喜欢的食物?"
        my_s = AnonymousSurvey(q)
        r = ['KFC', 'MDl', 'DKS']
        for i in r:
            my_s.store_response(i)
        for i in r:
            self.assertIn(i, my_s.responses)

# 开始点
if __name__ == '__main__':
    unittest.main()