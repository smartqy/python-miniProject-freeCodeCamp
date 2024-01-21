import random

# def make_new_board():
#         board = [[None for _ in range(5)] for _ in range(5)]
        
#         bombs_planted = 0
#         while bombs_planted < 5:
#             loc = random.randint(0, 24)
#             row = loc // 5
#             col = loc % 5

#             if board[row][col] == '*':
#                 continue

#             board[row][col] = '*'
#             bombs_planted += 1

#         return board

# a = make_new_board()
# for row in a[1]:
#      print(row)
#      print(type(row))
     
# print(make_new_board())

import re

# Given String
s = "I am a human being."

# Performing Split
res_1 = re.split('a', s)
res_2 = re.split('a', s, 1)

# Print Results
print(res_1)
print('this is new branch do')
print(1+1)
