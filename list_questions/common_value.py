list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
list3 = []
i=0
while i<len(list1):
    b=0
    while b<len(list2):
        if list1[i]==list2[b]:
            list3.append(list1[i])
        b=b+1
    i=i+1
print(list3)
list3.sort()
print(list3)

# esme jo common value h dono list me vo list3 me append kr rha h