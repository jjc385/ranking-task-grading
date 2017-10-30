from math import ceil
from scipy.stats import kendalltau

#### Grader Inputs

problem_point_value = 3

correct_string = "ABCDEF"


#### Code

def grade_ranking_task() :

    student_string = input( "Input the student's answer: " ).strip().upper()


    correct_answers = [letter for letter in correct_string]
    student_answers = [letter for letter in student_string]


    if sorted(student_answers) is not sorted(correct_answers) :
        print("Warning:  student answer is NOT a rearrangement of the correct answer")


    cypher = { letter:i for i,letter in enumerate(correct_answers) }

    student_numerical = [cypher[letter] for letter in student_answers]

    tau = kendalltau( [range(1,len(correct_answers)+1)], student_numerical)[0]

    if tau > 0:
        print("Student Score:", ceil((tau * problem_point_value) * 10) / 10)
    else:
        print("Student Score:", 0.0)


if __name__ == '__main__' :

    print( "This question is worth:\t", problem_point_value, "points" )
    print( "The correct answer is:\t", correct_string )
    print( "Note that student answers are not case sensitive.\n\n" )

    while True :
        grade_ranking_task()
        print()
