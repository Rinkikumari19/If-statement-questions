mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
# print(mainStr.split("over"))
# print(mainStr.strip("over"))
# print (len(mainStr))
x=mainStr.split()
print(x)
# print(len(x))
i = 0
new_list = []
while i < len(x):
    if x[i]!=('over'):
       new_list.append(x[i])
    i=i+1
# print(new_list)

i=0
while i<len(new_list):
    print(new_list[i] + " "),
    i=i+1







# replacementStr = "on"
# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# print(mainStr.replace('over','on'))

# remove = input("any word")
# add = input("any word")
# print(mainStr.replace(remove,add))

