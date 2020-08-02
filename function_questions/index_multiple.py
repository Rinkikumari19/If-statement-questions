def list_change(list1,list2):
    i=0
    new_list=[]
    while i<len(list1):
        new_list.append (list1[i]*list2[i])
        i=i+1
    print(new_list)
list_change([5, 10, 50, 20], [2, 20, 3, 5])