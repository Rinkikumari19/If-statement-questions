# elements = [23,14,56,12,19,9,15,25,31,42,43]
# i = 0
# odd = 0
# even = 0
# while i < len(elements):
#     if elements[i]%2==0:
#         even = even + 1
#     else:
#         odd = odd + 1
#     i = i + 1
# print(even)
# print(odd)
# ye code kitne odd or even number hai vo print krega


# elements = [23,14,56,12,19,9,15,25,31,42,43]
# i = 0
# odd_sum = 0
# even_sum = 0
# ave = 0
# ave1 = 0
# while i < len(elements):
#     if elements[i] % 2 == 0:
#         even_sum = even_sum + elements[i]
#         ave = ave + 1
#     else:
#         odd_sum = odd_sum + elements[i]
#         ave1 = ave1 + 1
#     i = i + 1
# print(even_sum/ave)
# print(odd_sum/ave1)

# is code me even_sum or odd_sum ka average print krega


elements = [23,14,56,12,19,9,15,25,31,42,43]
i = 0 
sum_odd = 0
sum_even = 0
ave = 0
ave1 = 0
while i < len(elements):
    if elements[i]%2==0:
        sum_even=sum_even+elements[i]
        ave=ave+1
    else:
        sum_odd=sum_odd+elements[i]
        ave1=ave1+1
    i = i + 1
print("odd number ka count:",ave1)
print("even number ka count:",ave)
print("sare number ka count:",ave1+ave)
print("odd number ka sum:",sum_odd)
print("even number ka sum:",sum_even)
print("sare number ka sum:",sum_odd+sum_even)
print("odd number ka avarage:",sum_odd/ave1)
print("even number ka avarage:",sum_even/ave)
print("sare numbers ka avarage:",(sum_even+sum_odd)/i)

# ye code sara kuchh print krega

