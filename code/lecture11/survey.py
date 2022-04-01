# 调查问卷类
class AnonymousSurvey:
    # 存储问题
    def __init__(self, question):
        self.question = question
        self.responses = []
    # 显示调查问卷
    def show_question(self):
        print(self.question)

    # 存储每份调查答案
    def store_response(self, new_response):
        self.responses.append(new_response)

    # 显示所有答卷
    def show_results(self):
       print("调查结果如下:")
       for r in self.responses:
           print(f"- {r}")