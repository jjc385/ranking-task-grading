## ranking-task-grading

Josh Samani's script for grading ranking tasks

### Updates

Some updates made by Jared.  The script now :

* Works for an answer string of any length
* Prompts the grader to input the student's answer
* Runs in an infinite loop so that the script need not be rerun for every student
* Warns the grader if the student answer is not a rearrangement of the correct answer
* Prints point value and correct answer at the start to remind the grader
* Allows for more than one correct answer
  * If more than one correct answer is supplied, the correct answer which
	generates the maximum student score is used
