marks = [43,67,9,21,90,34,76,23]
# list_length = len(marks)
index = 0
total_marks = 0
while index < len(marks):
    total_marks = marks[index]+total_marks
    index = index + 1
print ("total_marks:"+str(total_marks))

# total marks ko print krega