user = int(input("number"))
c = 0
num = 2
while c<user:
    a = 2
    while a*a<=num:
        while num%a ==0:
            num = num +1
        a=a+1
    print(num)
    num = num + 1
    c=c+1