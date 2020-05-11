# friends_name = ["swati","rinki","kritika","poonam","rabiya"]
# print(friends_name)
# print type(friends_name)

# number = [4,7,9,3,6,8,20]
# print(number)
# print type(number)


# mixed = [5,"bhai",3.7]
# print(mixed)
# print type(mixed)


# sisters_name = ["kiran","rakesh","rinki","pinki"]
# print sisters_name[0]
# sisters_name[1] = "anita"
# print(sisters_name)
# print len(sisters_name)


# Family_Members = ["shiv","anita","rakesh","kiran","rinki"]
# Family_Members.append("pinki")
# print (Family_Members)
# print len(Family_Members)
# if "chinki"in Family_Members:
#     print("hmmm")
# else:
#     print("nhi yrrr!!!")

 
# list = [6,8,0,1,2]
# list.pop()
# print (list)
# list.pop(3)
# print(list)


# students_name = ["shweta","urvashi","roshani","archana"]
# list_length = len(students_name)
# index = 0
# while index < (list_length):
#     print students_name[index]
#     index = index + 1


# marks = [43,67,9,21,90,34,76,23]
# # list_length = len(marks)
# index = 0
# total_marks = 0
# while index < len(marks):
#     total_marks = marks[index]+total_marks
#     index = index + 1
# print ("total_marks:"+str(total_marks))
# total marks ko print krega


# students_marks = [32,67,98,65,78,53,36,10,65,32]
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < len(students_marks):
#     if students_marks[index] < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print(less_than50)
# print(more_than50)


# numbers = [50,40,23,70,56,12,35,10,27]
# length = len(numbers)
# index = 0
# sum = 0
# while index < len(numbers):
#     if numbers[index] > 20 and numbers[index] < 40:
#         sum = sum + 1
#     index = index +1
# print(sum)
# ye sirf 20 or 40 ke bich ke value print krega



# state = ["delhi","gujrat","banglore","bihar","panjab"]
# state.reverse()
# print(state)
    # or
# p = -len(state)-1
# i = -1
# while i > p:
#     print(state[i]),
#     i = i - 1

# It will print reverse





# marks = [[78,76,94,86,88],[91,71,98,65,76,1,2],[95,45,78,52,49,5]]
# i = 0
# sum = 0
# a = 0
# while i<len(marks):
#     b = 0
#     while b < len(marks[i]):
#         sum = sum + marks[i][b]
#         b = b + 1
#     i = i + 1
# print(sum)
# It will print sum of all elements
 


# marks = [[78,76,94,86,88],[91,71,98,65],[95,45,78]]
# index = 0
# r = 0
# sum = 0
# while index < len(marks):
#     p = 0
#     while p < len(marks[index]):
#         sum = sum + marks[index][p]
#         p = p + 1
#     index = index + 1
#     print(sum)
# It is printing sum of seprate list




# marks = [[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
# i = 0
# sum = 0
# while i < len(marks):
#     k = 0
#     while k < len(marks[i]):
#         sum = sum + marks[i][k]
#         k = k + 1
#     i = i + 1
# print(sum)
# It is also printing sum of elements




# marks = [[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i = 0
# while i < len(marks):
#     b = 0
#     sum = 0
#     while b < len(marks[i]):
#         sum = sum + marks[i][b]
#         b=b+1
#     i = i + 1
#     print(sum/b)
# ye teeno sal ka marks ka avrage alag alag nikal rha hai
    


    
# marks = [[78, 76, 94, 86, 88], [91, 71, 98, 65],[95, 45, 78]]
# i = 0
# while i < len(marks):
#     s = 0
#     sum = 0
#     while s < len(marks[i]):
#         sum = sum + marks[i][s]
#         s = s + 1
#     i = i + 1
#     print(sum/s)  

# It will print avrange
    



# marks = [[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
# i = 0
# while i < len(marks):
#     a = 0
#     sum = 0
#     while a < len(marks[i]):
#         sum = sum + marks[i][a]
#         a = a + 1
#     i = i + 1
#     print(sum/a)
# It will check avrage of seprate list




# n = [10,11,12,13,14,17,18,19]
# i = 0
# while i < len(n):
#     b = i+1
#     while b < len(n):
#         if n[i]+n[b]==30:
#             print(n[i],n[b])
#         b=b+1
#     i=i+1
# output will come sum of 30 like (11,19)(12,18)(13,17)
    



# char_list = ["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# a = 0
# n = 0
# t = 0
# x = 0
# u = 0
# g = 0
# i = 0
# while i < len(char_list):
#     if char_list[i]==("a"):
#         a=a+1
#     elif char_list[i]==("n"):
#         n=n+1
#     elif char_list[i]==("t"):
#         t=t+1
#     elif char_list[i]==("x"):
#         x=x+1
#     elif char_list[i]==("u"):
#         u=u+1
#     else:
#         g=g+1
#     i=i+1
# print("a",a)
# print("n",n)
# print("t",t)
# print("x",x)
# print("u",u)
# print('g',g)

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




# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# for i in range(len(big_list)):
#         print("...")
#         for j in range (len(big_list[i])):
#                 print(big_list[i][j],end="")
#         print("\n")
# ye list ki sari elements print krega string data me





