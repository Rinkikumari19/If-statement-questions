list1 = [4.9,"pinki",5,"4",8.3,"7.43","9"]
string=[]
float1 = []
integer = []
for i in range(len(list1)): 
    if type(list1[i]) == int:
        integer.append(list1[i])
    elif type(list1[i]) == float:
        float1.append(list1[i])
    else:
        string.append(list1[i])
print(string)
print(integer)
print(float1)