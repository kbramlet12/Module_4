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


exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: "))

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one exam_two exam_three]
sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C'
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print "Student is failing."
else:
    print "Student is passing."
