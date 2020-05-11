n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
new_list=[]
i = 0
new_list.append(n[0])
while i < len(n):
    a = 0
    flag=True
    while a < len(new_list):
        if n[i]==new_list[a]:
            flag=True
            break
        else:
            a=a+1
            flag=False
    if flag==False:
        new_list.append(n[i])
    i=i+1
# print(new_list)

a = 0
count=0
while a < len(new_list):
    i=0
    count=0
    list=[]
    while i<len(n):
        if new_list[a]==n[i]:
            count = count+1
        i=i+1
  
    if count>1:
        list.append(new_list[a])
    a=a+1
    print(list)



