# Program Name: grading.py
# Purpose of a program:
# Write a program computing an average of three exam scores
# User enters three exam scores.
# Program prints the exam scores, average of three scores, corresponding letter grade,
# and result of Pass or Fail of a course.


# To pass a course, student should get a grade C or above.

# Average Score    Grade
#    90+	        A
#    80-89	        B
#    70-79	        C
#    60-69	        D
#    0-59	        F

# Example of output
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.


exam_1 = int(input("Input your grade for Exam 1: "))

exam_2 = int(input("Input your grade for Exam 2: "))

exam_3= int(input("Input your grade for Exam 3: "))

Exam_grades = [exam_1, exam_2, exam_3]
list_length= len(Exam_grades)
sum_of_exam_grades= 0
for i in range(list_length):
    sum_of_exam_grades= sum_of_exam_grades+Exam_grades[i]
Average = sum_of_exam_grades/3

if Average >= 90:
    letter_grade = "A"
elif Average >= 80 and Average < 90:
    letter_grade = "B"
elif Average >= 70 and Average < 80:
    letter_grade = "C"
elif Average >= 60 and Average < 70:
    letter_grade = "D"
elif Average < 60:
    letter_grade = "F"


print("Exam Scores:", Exam_grades)
print("Average:", Average)
print("Grade:", letter_grade)
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")


#1 The first thing I did was look for basic syntax and formatting errors. I think I may know how to fix this one without running it at all I will see.
#2 After getting rid of some things and retyping some lines, I think I have it formatted a little more simple to hopefully get the correct output.
#3 I had a couple minor syntax errors that I missed like a ":" after 70
#4 I had a little trouble with the sums, but I think I figured it out
#5 It works!!
#AUTHOR: Keegan Bramlet
#DATE: 10/30/2022
