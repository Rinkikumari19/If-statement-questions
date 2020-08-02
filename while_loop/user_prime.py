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