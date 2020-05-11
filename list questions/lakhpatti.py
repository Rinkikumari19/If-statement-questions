kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i = 0
paisa = kitna_paisa_hai
length = len(kitna_paisa_hai)
num = 0
num1 = 0
num2 = 0
while i < length:
    if paisa[i] >= 10000000:
        num = num + 1
    elif paisa[i] >= 100000:
        num1 = num1 + 1
    else:
        num2 = num2 + 1
    i = i + 1
print("Crorepati hai:",num)
print("Lakhpati hai:",num1)
print("dilwale hai",num2)

        