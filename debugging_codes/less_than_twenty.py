def numbers_less_than_twenty(list):
    counter = 0
    new_list=[]
    while counter < len(list):
        item = list[counter]
        if item < 20:
            new_list.append(list[counter])
        else:
            print("")
        counter += 1
    return new_list
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
