string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
list1 = string_list
new_list = []
index=0
while index < len(list1):
    if list1[index] not in new_list:
        new_list.append(list1[index])
    index=index+1
print(new_list)