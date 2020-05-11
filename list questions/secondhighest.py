# numbers = [56,40,60,6,12,10,7,32,5]
# index = 0
# max = 0
# max2 = 0
# while index < len(numbers):
#     if numbers[index] > max:
#         max = numbers[index]
#     index = index+1
# maxium = max
# i = 0
# while i < len(numbers):
#     if max > numbers[i] and max2 < numbers[i]:
#         max2 = numbers[i]
#     i = i + 1
# print (max2)  
# esse second highest number print hoga


# numbers.sort()
# print(numbers)
# print(numbers[-2])

# this is another code

# a = 0
# num = 5
# max = 0
# max2 = 0
# while a < num:
#     user = input("enter your number")
#     if user > max:
#         max = user
#     a = a + 1
# maximum = max
# i = 0
# max2 = 0
# while i <= num:
#     if user > max2:
#         max=user
#     i=i+1
# if user>max2 and max2<maximum:
#     print (max2)


# i = 0
# max = 0
# max2 = 0
# while i < len(numbers):
#     if (numbers[i])>max:
#         max2=max
#         max = numbers[i]

#     elif max > (numbers[i]) and numbers[i] > max2:
#         max2 = numbers[i]
#     i=i+1
# print(max2)


a = 0
max = 0
max2 = 0
while a < 10:
    user = int(input("enter your number "))
    if user>max:
        max2 = max
        max = user
    elif user<max and max2<user:
        max2 = user
    a=a+1
print(max2)
