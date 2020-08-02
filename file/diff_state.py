my_file  = open("question3.txt","r")
# print my_file.readline():
for i in my_file:
    
    if "delhi" in i: 
        my_data=open("delhi.txt",'a')
        my_data.write(i)
    elif "shimla" in i:
        my_data = open("shimla.txt",'a')
        my_data.write(i)
    else:
        my_data=open("others.txt",'a')
        my_data.write(i)
my_file  = open("others.txt",'r')
print("data for delhi from delhi.txt file")
for i in my_file:
    print(i)




