# 1. Student Attendance Analyzer
# Write a Python program that takes attendance percentages of 10 students using a loop. Create a function count_eligible_students() that counts how many students have attendance greater than or equal to 75%. Requirements:
# ● Use a for loop for input collection.
# ● Use a function with one argument.
# ● Return the count from the function.
# ● Display the result.

def count_eligible_students(attendance_list):
    count = 0
    for attendance in attendance_list:
        if attendance >= 75:
            count += 1
    return count

attendances = []

for i in range(10):
    percentage = float(input(f"Enter attendance percentage of student {i+1}: "))
    attendances.append(percentage)

eligible_students = count_eligible_students(attendances)

print("Number of eligible students:", eligible_students)