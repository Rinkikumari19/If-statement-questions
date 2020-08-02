list = [[5,6,9],[2,4],[10],[12,14,18]]
i=0
new_list=[]
while i <len(list):
    nes_index = 0
    while nes_index < len(list):
        if list[i][nes_index] % 2 == 0:
            new_list.append(list[i][nes_index])
           
        nes_index=nes_index+1
    i=i+1
print(new_list)
