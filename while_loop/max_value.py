a=0
max = int(input("number"))
while a<10:
    user = int(input("enter your number"))
    if user>max:
        max=user
    a=a+1
print(max)