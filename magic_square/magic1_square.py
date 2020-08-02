
def if_magic_square(magic_square):
    sum = 0 
    i = 0
    while i < len(magic_square):
        sum = sum + (magic_square[i][i])
        i = i + 1
    
    i = 0
    sum2 = 0
    p = len(magic_square)-1
    while i < len(magic_square):
        sum2 = sum2 + (magic_square[i][p])
        i = i + 1
        p = p - 1
    if sum != sum2:
        return False
    i = 0
    sum3 = 0
    while i < len(magic_square):
        b = 0
        while b < len(magic_square[i]):
            sum3 = sum3 + (magic_square[i][b])
            b = b + 1
        if sum3 != sum2:
            return False
        i = i + 1
    
    i = 0
    sum4 = 0
    while i < len(magic_square):
        c = 0
        while c < len(magic_square[i]):
            sum4 = sum4 + (magic_square[c][i])
            c = c + 1
            if sum4 != sum4:
                return False
            i = i + 1
        return True
magic_square = [[5, 3, 7],[1, 8, 9],[6, 4, 2]]
print(if_magic_square(magic_square))