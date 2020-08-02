
marks = [[78,76,94,86,88],[91,71,98,65,76,1,2],[95,45,78,52,49,5]]
i = 0
sum = 0
a = 0
while i<len(marks):
    b = 0
    while b < len(marks[i]):
        sum = sum + marks[i][b]
        b = b + 1
    i = i + 1
print(sum)
# It will print sum of all elements