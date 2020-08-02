user = int(input("enter your number "))
if len(user)>6 and len(user)<16:
    if "$" in user:
        if "A" and "Z" in user:
            print("strong password")
        else:
            print("weak password")
    else:
        print("weak password")
else:
    print("weak password")