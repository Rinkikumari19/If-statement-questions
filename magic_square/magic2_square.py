def if_magic_square(magic_square):
    i = 0
    sum = 0
    while i < len(magic_square):
        sum = sum + magic_square[i][i]
        i = i + 1

    i = 0
    sum2 = 0
    p = len(magic_square)-1
    while i < len(magic_square):
        sum2 = sum2 + magic_square[i][p]
        i = i + 1
        p = p - 1
    if sum != sum2:
        return False

    i = 0
    sum3 = 0
    r = 0
    while i < len(magic_square):
        while r < len(magic_square[i]):
            sum3 = sum3 + magic_square[i][r]
            r = r + 1
        if sum3 != sum2:
            return False
            i = i + 1

    i = 0
    a = 0
    sum4 = 0
    while i < len(magic_square):
        while a < len(magic_square[i]):
            sum4 = sum4 + magic_square[a][i]
            a = a + 1
        if sum4 != sum3:
            return False
            i = i + 1
        return True

magic_square = [[8, 3, 4, 0],[1, 5, 9],[6, 7, 2]]
print(if_magic_square(magic_square))


  

   

