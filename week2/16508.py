import sys

input = sys.stdin.readline

# 적은 비용으로 원하는 단어 만들기
target = str(input()).strip()
num_of_books = int(input())

price = []
name = []
for _ in range(num_of_books):
    x, y = input().split()
    price.append(int(x))
    name.append(str(y))

'''
단어 만들기
1. 한 책에서 더하기
2. 각 책들에서 더하기
'''

min_price = int(1e9)

# book index에 따라 몇 번째 알파벳에 들어가 있는지 확인
# target의 알파벳 위치 별로 리스트의 해당 인덱스에 추가
candidates = [[] for i in range(len(target))]

for i in range(len(name)):
    for j in range(len(target)):
        if target[j] in name[i]:
            candidates[j].append(i)

print(candidates)  # [[0, 1, 3], [2, 3], [0, 1, 2, 3]]
