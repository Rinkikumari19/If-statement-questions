num = int(input("number"))
num2 = int(input("number"))
num3 = int(input("number"))
if num>num2:
    if num<num3:
        print(num)
    else:
        if num2>num3:
            print(num2)
        else:
            print(num3)
else:
    if num>num3:
        print(num)
    else:
        if num3>num:
            if num2>num3:
                print(num3)
            else:
                print(num2)
        else:
            print(num)