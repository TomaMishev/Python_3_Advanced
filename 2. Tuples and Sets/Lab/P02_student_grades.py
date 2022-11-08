# Write a program that reads students' names and their grades and adds them to the student record. On the first line,
# you will receive the number of students – N. On the following N lines, you will be receiving a student's name and
# their grade. For each student print all his/her grades and finally his/her average grade, formatted to the second
# decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})". The order
# in which we print the result does not matter.

n = int(input())
student_grades = dict()
for _ in range(n):
    name, grade = input().split(" ")
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(float(grade))
for kvp in student_grades.items():
    print(f"{kvp[0]} -> {' '.join([f'{x:.2f}' for x in kvp[1]])} (avg: {sum(kvp[1]) / len(kvp[1]):.2f})")