marks = [[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
i = 0
while i < len(marks):
    a = 0
    sum = 0
    while a < len(marks[i]):
        sum = sum + marks[i][a]
        a = a + 1
    i = i + 1
    print(sum/a)
# It will check avrage of seprate list



