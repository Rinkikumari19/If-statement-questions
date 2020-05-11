num = int(input("enter your number"))
result = 0
i = 1
while (i<=num):
    if (num%i==0):
        result = result + 1
    i=i+1
if (result == 2):
    print("prime")
else:
    print("not prime")





# a = 2
# while a <= 100:
#     b = 2
#     while b < a:
#         if a%b == 0:
#             break
#         b=b+1
#     else:
#         print(a)
#     a=a+1



    
