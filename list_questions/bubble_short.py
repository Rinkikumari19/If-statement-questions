number = [-2,45,0,-8,11,-9,2]
n=0
while n<len(number):
    i=0
    while i<len(number)-1:
        if number[i] > number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
        else:
            number[i],number[i+1]=number[i],number[i+1]
        i=i+1
    n=n+1
print(number)

# ye phle ek bar run kr rha h fir usi ko kyi bar run kr rha h

        
