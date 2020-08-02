marks = [[78,76,94,86,88],[91,71,98,65],[95,45,78]]
index = 0
r = 0
sum = 0
while index < len(marks):
    p = 0
    while p < len(marks[index]):
        sum = sum + marks[index][p]
        p = p + 1
    index = index + 1
    print(sum)
# It is printing sum of seprate list