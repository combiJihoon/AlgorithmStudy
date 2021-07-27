import sys
from itertools import product

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(str, input().split()))
length = len(str(n))

max_num = -1
while length != 0:
    tmp = list(product(arr, repeat=length))
    for i in tmp:
        num = ''.join(i)
        num = int(num)

        if num <= n:
            max_num = max(max_num, num)

    length -= 1

print(max_num)


'''시간초과'''
# num_list = []
# for i in K:
#     for j in K:
#         for k in K:
#             num = i + j + k
#             new_num = int(num)
#             if new_num <= n:
#                 num_list.append(new_num)

# num_list.sort()
# print(num_list[-1])

# def findNum(n, K):
#     for i in range(n, 0, -1):
#         target = str(i)
#         is_havingK = True
#         for t in target:
#             if t not in K:
#                 is_havingK = False
#                 break
#         if is_havingK:
#             return i

# print(findNum(n, K))
