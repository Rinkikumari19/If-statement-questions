
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
new_list=[]
i=0
while i < len(string_list):
    if string_list[i] not in new_list:
        new_list.append(string_list[i])
    i=i+1
print(new_list)