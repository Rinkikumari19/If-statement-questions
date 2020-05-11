str1 = input("str1 ")
str2 = input("str3 ")
# if len(str1)==len(str2):
#     for i in range(0,len(str1)):
#         if str1[i] in str2:
#             i=i+1
#         else:
#             print("This is not anagram")
#             break
#     else:
#         print("This is anagram")
# else:
#     print("This is not anagram")

            # OR

            
sort1 = sorted(str1)
sort2 = sorted(str2)
if len(str1)==len(str2):
    if sort1==sort2:
        print('This is anagram')
    else:
        print("This is not anagram")
else:
    print("This is not anagram")