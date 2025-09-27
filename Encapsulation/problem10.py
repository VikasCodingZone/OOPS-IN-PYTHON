# Q10. Online Exam System
# Ek Exam class banao jisme private dictionary __questions ho (QnA store kare).
# Method add_question(q, ans) → question add kare.
# Method attempt(q, ans) → agar sahi hai to "Correct" else "Wrong".
# Method get_all_questions() → available questions return kare.

class Exam:
    def __init__(self):
        self.__questions = {}

    def add_question(self, q, ans):
        self.__questions[q] = ans

    def attempt(self, q, ans):
        if q in self.__questions:
            if self.__questions[q] == ans:
                return "Correct"
            else:
                return "Wrong"
        return "Question not found"

    def get_all_questions(self):
        return list(self.__questions.keys())


exam = Exam()
exam.add_question("Capital of India?", "Delhi")
print(exam.attempt("Capital of India?", "Delhi"))
print(exam.get_all_questions())
