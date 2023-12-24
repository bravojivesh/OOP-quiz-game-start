#the benfit of this is we do not have to create too many attributes. (see lines 6 and 7 being commented out)
# calling one function within another and passing arguments (line 26, 29, 30)

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        # self.user_answer = ""
        # self.right_answer = ""
        self.score = 0

    def still_has_questions(self):
        length = len(self.question_list)
        return self.q_num < length
        # the above is same as saying "if condition return True else return False"

    def next_question(self):
        current_question = self.question_list[self.q_num]
        # ask= input (f"{current_question["text"]} True/False: ")
        # JH: above is how I wrote earlier. The "text" part would be WROng.
        # Reason: question_list WILL BE question bank with a list of "Question class objects"
        # So we need to write "current_question.text" (following Question class attributes.
        ask = input(f"Q{(self.q_num) + 1}. {current_question.text} True/False: ")
        right_ans= current_question.answer
        self.q_num += 1
        self.count_score(ask,right_ans)


    def count_score(self, user_ans,right_ans):
        if user_ans.lower()== right_ans.lower():
            self.score += 1
            print(f" Correct! Your current score is {self.score}/{self.q_num} ")
        else:
            print(f" Wrong! Your current score is {self.score}/{self.q_num} ")