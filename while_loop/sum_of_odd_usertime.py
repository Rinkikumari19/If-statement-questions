n = int(input("enter your number"))
a=1
sum=0
count = 0
max = n*2
while a<=n*n:
    if a%2==1:
        sum=sum+a
        count=count+1
        if count == n:
            break 
    a=a+1
print(sum)