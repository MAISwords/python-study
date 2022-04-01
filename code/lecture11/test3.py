# 运行类
from survey import AnonymousSurvey

q = "你喜欢的食物是什么?"
my_survey = AnonymousSurvey(q)

# 显示问题，并且存储答案
my_survey.show_question()
print("输入q退出!")

# 进入循环体
while True:
    re = input("\n食物:")
    if re == 'q':
        break
    my_survey.store_response(re)

print("感谢您参与本次调查!")
my_survey.show_results()

