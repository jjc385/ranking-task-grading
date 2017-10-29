# Grader Inputs

problem_point_value = 5

correct_string = "ABCDEF"
student_string = "ABCDEF"

# Code

from math import ceil
from scipy.stats import kendalltau

correct_answers = [letter for letter in correct_string]
student_answers = [letter for letter in student_string]

cypher = {correct_answers[0]:1, correct_answers[1]:2, correct_answers[2]:3, correct_answers[3]:4, correct_answers[4]:5, correct_answers[5]:6}

student_numerical = [cypher[letter] for letter in student_answers]

tau = kendalltau([1,2,3,4,5,6], student_numerical)[0]

if tau > 0:
    print("Student Score:", ceil((tau * problem_point_value) * 10) / 10)
else:
    print("Student Score:", 0.0)
