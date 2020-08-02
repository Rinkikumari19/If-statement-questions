char_list = ["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
a = 0
n = 0
t = 0
x = 0
u = 0
g = 0
i = 0
while i < len(char_list):
    if char_list[i]==("a"):
        a=a+1
    elif char_list[i]==("n"):
        n=n+1
    elif char_list[i]==("t"):
        t=t+1
    elif char_list[i]==("x"):
        x=x+1
    elif char_list[i]==("u"):
        u=u+1
    else:
        g=g+1
    i=i+1
print("a",a)
print("n",n)
print("t",t)
print("x",x)
print("u",u)
print('g',g)

        # OR

# i = 0
# new_list = []
# new_list.append(char_list[0])
# while i < len(char_list):
#     b = 0
#     flag = True
#     while b < len(new_list):
#         if char_list[i]==new_list[b]:
#             flag = True
#             break
#         else:
#             b=b+1
#             flag=False
#     if flag == False:
#         new_list.append(char_list[i])
#     i=i+1

# new_index = 0
# while new_index < len(new_list):
#     i = 0
#     count = 0
#     while i < len(char_list):
#         if new_list[new_index]==char_list[i]:
#             count = count + 1
#         i = i + 1
#     print(new_list[new_index],count)
#     new_index = new_index + 1



        #  OR


# new_list=[]
# i=0
# while i < len(char_list):

#     if char_list[i] not in new_list:
#         new_list.append(char_list[i])
#     i=i+1
# print(new_list)

        # OR

# new_list = set(char_list)
# print(new_list)

# It will print count of elements