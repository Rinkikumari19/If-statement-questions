
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
bank_file = open("bank.txt","w")
for ele in banks_list:
    bank_file.write(ele)
    bank_file.write("\n")
i=0
while i<len(banks_list):
    print(banks_list[i])
    i=i+1
bank_file = open("bank.txt",'r')
my_data = bank_file.read()
print(my_data)








