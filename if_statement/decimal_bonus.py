user=int(input("enter your number"))
if user<100:
    print(0.015*user)
elif user>100 and user<150:
    print((0.015*user)+(0.002*user))
elif user>150:
    print((0.015*user)+(0.02*user)+(0.03*user))