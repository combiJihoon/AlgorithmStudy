# # 16508번 풀이
# from itertools import product
# import sys


# def checkBook(word, book, price):
#     cnt = 0
#     for w in word:
#         if w in book:
#             cnt += 1
#             book = book.replace(w, ' ', 1)
#             if cnt == len(word):
#                 return price
#     return sys.maxsize


# def solution():
#     ret = []
#     T = sys.stdin.readline().strip()
#     N = int(sys.stdin.readline())
#     price = []
#     book = []
#     for _ in range(N):
#         p, b = map(str, sys.stdin.readline().split())
#         price.append(int(p))
#         book.append(b)

#     for i in range(1 << len(book)):
#         searchString = ""
#         sumPrice = 0
#         for j in range(len(book)):
#             what = (i & 1 << j)
#             if what != 0:
#                 searchString += book[j]
#                 sumPrice += price[j]
#         ret.append(checkBook(T, searchString, sumPrice))

#     ret = min(ret)
#     if ret == sys.maxsize:
#         ret = -1

#     print(ret)


# solution()


"""
- 전공책
완전탐색 문제 -> 모든 케이스를 정리하고 각 값을 비교!
"""

import sys
from itertools import product

input = sys.stdin.readline
price = list()
title = list()

word = input().strip()
book_cnt = int(input())

for _ in range(book_cnt):
    p, t = input().split()
    price.append(int(p))
    title.append(t)

total = 1600001
# 이 부분은 비트연산자로 해결하는 방법 연구할 필요가 있음
cases = [x for x in product([0, 1], repeat=book_cnt)]
print(cases)


def check_word(titles, ans):
    for w in word:
        if w not in titles:
            return 1600001
        else:
            # 틀린 이유
            # "titles = " 이 부분이 없어서 titles를 replace한 titles가 반영이 안됨
            # titles를 바꿔줘야 함! (replace한 값을 저장)
            titles = titles.replace(w, "", 1)
    return ans


for case in cases:
    titles = ""
    ans = 0
    for i in range(len(case)):
        if case[i] == 1:
            titles += title[i]
            ans += price[i]
    total = min(check_word(titles, ans), total)
    # print(case, titles, ans, check_word(titles, ans))

print(total if total != 1600001 else -1)
