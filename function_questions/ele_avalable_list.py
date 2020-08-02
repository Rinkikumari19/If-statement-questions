list = []
for i in range(0,10):
# we have to take 10 times input from user and then we have to append in list
    user = input("enter any number")
    list.append(user)
print(list)

# then again we have to take input from user and we will check that it is number avalable in list or not
user = input("any number")
if user in list:
    print("yes",user)
else:
    print("nahi",user)
