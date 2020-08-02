
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter your number"))
if a>b:
    if a>c:
        print(a)
    elif c>b:
        print(c)
elif b>c:
    print(b)
elif c>a:
    if c>b:
        print(c)
    elif b>a:
        print(b)
    # esme sabse highest number print kr rha hai