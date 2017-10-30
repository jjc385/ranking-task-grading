# Grader Inputs

problem_point_value = 3

correct_string = "ABCDEF"
student_string = "ABCDEF"

# Code

from math import ceil
from scipy.stats import kendalltau

correct_answers = [letter for letter in correct_string]
student_answers = [letter for letter in student_string]

cypher = { letter:i for i,letter in enumerate(correct_answers) }

student_numerical = [cypher[letter] for letter in student_answers]

tau = kendalltau( [range(1,len(correct_answers)+1)], student_numerical)[0]

if tau > 0:
    print("Student Score:", ceil((tau * problem_point_value) * 10) / 10)
else:
    print("Student Score:", 0.0)
