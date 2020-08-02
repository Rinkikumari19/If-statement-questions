i = 1
while i<11:
    user =int(input("enter your number"))
    if user < 5:
        print("aapka number chhota hai")
    elif user > 5:
        print("user bada hai")
    elif user == 5:
        print("user ne guess kr liya")
        break
    i=i+1
else:
    print("user guess nhi kr paya")



   
  

