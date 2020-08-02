a = 1
while a<6:
    user = int(input("enter your number"))
    if user == 5:
        print("guess kr liya")
        break
    a=a+1
else:
    print("user ne guess nhi kiya")