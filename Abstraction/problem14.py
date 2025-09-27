# Q14. Online Exam (MCQ vs Coding Test)

from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def start(self):
        pass

class MCQExam(Exam):
    def start(self):
        return "Starting Multiple Choice Exam"

class CodingExam(Exam):
    def start(self):
        return "Starting Coding Test"

e = CodingExam()
print(e.start())

# Q14. Online Exam (MCQ vs Coding Test)
# Common feature: exam start karna.
# Lekin MCQ exam aur coding exam ka interface alag hota hai.
# Abstraction → start() method common.