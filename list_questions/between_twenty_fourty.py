numbers = [50,40,23,70,56,12,35,10,27]
length = len(numbers)
index = 0
sum = 0
while index < len(numbers):
    if numbers[index] > 20 and numbers[index] < 40:
        sum = sum + 1
    index = index +1
print(sum)
# ye sirf 20 or 40 ke bich ke value print krega