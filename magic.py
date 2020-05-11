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


# def if_magic_square(magic_square):
#     sum = 0 
#     i = 0
#     while i < len(magic_square):
#         sum = sum + (magic_square[i][i])
#         i = i + 1
    
#     i = 0
#     sum2 = 0
#     p = len(magic_square)-1
#     while i < len(magic_square):
#         sum2 = sum2 + (magic_square[i][p])
#         i = i + 1
#         p = p - 1
#     if sum != sum2:
#         return False
#     i = 0
#     sum3 = 0
#     while i < len(magic_square):
#         b = 0
#         while b < len(magic_square[i]):
#             sum3 = sum3 + (magic_square[i][b])
#             b = b + 1
#         if sum3 != sum2:
#             return False
#         i = i + 1
    
#     i = 0
#     sum4 = 0
#     while i < len(magic_square):
#         c = 0
#         while c < len(magic_square[i]):
#             sum4 = sum4 + (magic_square[c][i])
#             c = c + 1
#             if sum4 != sum4:
#                 return False
#             i = i + 1
#         return True
# magic_square = [[5, 3, 7],[1, 8, 9],[6, 4, 2]]
# print(if_magic_square(magic_square))


# def if_magic_square(magic_square):
#     i = 0
#     sum = 0
#     while i < len(magic_square):
#         sum = sum + magic_square[i][i]
#         i = i + 1

#     i = 0
#     sum2 = 0
#     p = len(magic_square)-1
#     while i < len(magic_square):
#         sum2 = sum2 + magic_square[i][p]
#         i = i + 1
#         p = p - 1
#     if sum != sum2:
#         return False

#     i = 0
#     sum3 = 0
#     r = 0
#     while i < len(magic_square):
#         while r < len(magic_square[i]):
#             sum3 = sum3 + magic_square[i][r]
#             r = r + 1
#         if sum3 != sum2:
#             return False
#             i = i + 1

#     i = 0
#     a = 0
#     sum4 = 0
#     while i < len(magic_square):
#         while a < len(magic_square[i]):
#             sum4 = sum4 + magic_square[a][i]
#             a = a + 1
#         if sum4 != sum3:
#             return False
#             i = i + 1
#         return True

# magic_square = [[8, 3, 4, 0],[1, 5, 9],[6, 7, 2]]
# print(if_magic_square(magic_square))


  

   






