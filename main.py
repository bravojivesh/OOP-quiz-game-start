from question_model import Question
from data import question_data

length= len(question_data)
# print (length)

question_bank=[]

for i in range(length):
    question= question_data[i]["text"] #extracting the question part only
    answer= question_data[i]["answer"] #extracting the answer part only
    qna=Question(question,answer) #a new variable to store Question object. Note this changes
    #with every value of i. So we need to store all the values. Look below.
    question_bank.append(qna) #cont: so we need a list to store all the objects.

print (question_bank[11].text)


