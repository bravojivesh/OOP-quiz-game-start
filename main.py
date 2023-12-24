from question_model import Question
from data import question_data
# from quiz_brain import QuizBrain
from question_brain2 import QuizBrain
#JH: Either import brain2 or brain. They are variations.

length= len(question_data)
# print (length)

question_bank=[]

for i in range(length):
    question= question_data[i]["text"] #extracting the question part only
    answer= question_data[i]["answer"] #extracting the answer part only
    qna=Question(question,answer) #a new variable to store Question object.
    # Note: this is only one record.This changes with every value of i.
    # So we need to store all the values. Look below.
    question_bank.append(qna) #cont: so we need a list to store all the objects.

# print (question_bank[11].text)

q_list= QuizBrain(question_bank)

while q_list.still_has_questions():
    q_list.next_question()
    # q_list.count_score() #Only Needed with brain (not with brain 2)

print (f"final score is: {q_list.score}/{q_list.q_num}")