
def check_number_list(list1,list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if i == j:
                if list1[i]%2==0 and list2[j]%2==0:
                    print("dono even hai")
                else:
                    print("dono even nhi hai")
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

# It will check same index value are even or not


