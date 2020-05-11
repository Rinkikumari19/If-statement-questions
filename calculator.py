def calculator(number_x,number_y,operation):
    if operation == "add":
        print(number_x + number_y)
    elif operation == "subtract":
        print(number_x - number_y)
    elif operation == "multiple":
        print(number_x * number_y)
    elif operation == "divide":
        print(number_x % number_y)
number_1 = calculator(24,20,"add")
number_2 = calculator(50,60,"multiple")
number_3 = calculator(80,120,"divide")
number_4 = calculator(90,23,"subtract")
calculator(15,10,"subtract")



# def calculator(number_x,number_y,operation):
#     if operation == "add":
#         print(number_x + number_y)
#     elif operation == "subtract":
#         print(number_x - number_y)
#     elif operation == "multiple":
#         print(number_x * number_y)
#     elif operation == "divide":
#         print(number_x % number_y)
# user = input("enter any number ")
# user1 = input("enter any number ")
# add_result = calculator(user,user1,"add")
# sub_result = calculator(user,user1,"subtract")
# mult_result = calculator(user,user1,"multiple")
# div_result = calculator(user,user1,"divide")


# def list_change(list1,list2):
#     i=0
#     new_list=[]
#     while i<len(list1):
#         new_list.append (list1[i]*list2[i])
#         i=i+1
#     print(new_list)
# list_change([5, 10, 50, 20], [2, 20, 3, 5])


a=2
b=1
c="*"
d="="
while b<=10:
    print(a,c,b,d,(a*b))
    b=b+1


