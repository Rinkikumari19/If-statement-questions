
students_marks = [32,67,98,65,78,53,36,10,65,32]
index = 0
less_than50 = 0
more_than50 = 0
while index < len(students_marks):
    if students_marks[index] < 50:
        less_than50 = less_than50 + 1
    else:
        more_than50 = more_than50 + 1
    index = index + 1
print(less_than50)
print(more_than50)