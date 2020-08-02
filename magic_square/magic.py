def if_magic_square(magic_square):
    sum = 0
    i = 0
    while i < len(magic_square):
        sum = sum + (magic_square[i][i])
        i = i + 1

    i = 0
    sum1 = 0
    j = len(magic_square[i])-1
    while i < len(magic_square):
        sum1 = sum1 + (magic_square[i][j])
        i = i + 1
        j = j - 1
    if sum != sum1:

        i = 0
    while i < len(magic_square):
        j = 0
        sum2 = 0
        while j < len(magic_square[i]):
            sum2 = sum2 + (magic_square[i][j])
            j = j + 1
        if sum != sum2:
            return False
        i = i + 1

    i = 0
    while i < len(magic_square):
        j = 0
        sum3 = 0
        while j < len(magic_square[i]):
            sum3 = sum3 + (magic_square[j][i])
            j = j + 1
        if sum3 != sum:
            return False
        i = i + 1

    return True

magic_square=[[8,3,4],[1,5,9],[6,7,2]]
print (if_magic_square(magic_square))









