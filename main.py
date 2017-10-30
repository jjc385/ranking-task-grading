from math import ceil
from scipy.stats import kendalltau

#### Grader Inputs

problem_point_value = 3

# All of the strings in this list are correct.
correct_strings = [
        "ABCDEF"
        ]


#### Code

def grade_ranking_task() :

    student_string = input( "Input the student's answer: " ).strip().upper()


    correct_answers = [[letter for letter in correct_string] for correct_string in correct_strings ]
    student_answer = [letter for letter in student_string]


    correct_form = False
    for correct_answer in correct_answers :
        if sorted(student_answer) == sorted(correct_answer) :
            correct_form = True
            break
    if not correct_form :
        print("Warning:  student answer is NOT a rearrangement of the correct answer")


    tau_max = 0.0
    for correct_answer in correct_answers :
        cypher = { letter:(i+1) for i,letter in enumerate(correct_answer) }

        student_numerical = [cypher[letter] for letter in student_answer]

        tau = kendalltau( [range(1,len(correct_answer)+1)], student_numerical)[0]

        if tau > tau_max :
            tau_max = tau

    print("Student Score:", ceil((tau_max * problem_point_value) * 10) / 10)


if __name__ == '__main__' :

    print( "This question is worth:\t", problem_point_value, "points" )
    print( "The possible correct answers are:\t", correct_strings )
    print( "Note that student answers are not case sensitive.\n\n" )

    while True :
        grade_ranking_task()
        print()
