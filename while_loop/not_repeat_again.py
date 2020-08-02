string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
new_list=[]
i=0
while i<len(string_list):
    if string_list[i] not in new_list:
        new_list.append(string_list[i])
    i=i+1
print(new_list)

# es list me vo elements print krega jo dubara repeat nahi hoga 