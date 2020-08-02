my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
my_file3 = open("test_file.txt",'r')
my_data6 = my_file3.read()
print(my_data6)
my_file3.close()
my_file3.write("Kuch aur likhte hain")  #ye line error show krega kyuki file close ho chuka h
