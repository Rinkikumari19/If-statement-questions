def add_sum_list(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i==j:
                print(list1[i]+list2[j])

add_sum_list([50, 60, 10],[10, 20, 13])
# It will add same index value