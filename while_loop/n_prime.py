a = 2
count = 0
n = int(input("num"))
while a<n*n:
    b = 2
    while b < a:
        if a%b == 0:
            break
        b=b+1
    else:
        print(a)
        count = count+1
        if count == n:
            break
    a=a+1