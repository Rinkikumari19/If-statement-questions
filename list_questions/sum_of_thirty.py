n = [10,11,12,13,14,17,18,19]
i = 0
while i < len(n):
    b = i+1
    while b < len(n):
        if n[i]+n[b]==30:
            print(n[i],n[b])
        b=b+1
    i=i+1
# output will come sum of 30 like (11,19)(12,18)(13,17)