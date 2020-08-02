file1 = open("people1_exercise.txt", 'r')

count = 0
for line in file1:
    print(line)
    count=count+1
print(count)
file1.close()

