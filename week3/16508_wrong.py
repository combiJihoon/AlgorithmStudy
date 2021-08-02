from itertools import product
import sys

'''
<product>
데카르트 곱이라고도 하는 cartesian product를 표현할 때 사용하는 메소드
(DB의 join, 관계 대수의 product를 생각하면 된다). 
이 메소드의 특징은 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다.
'''

input = sys.stdin.readline

# 입력
target = str(input()).strip()
n = int(input())
prices = []
titles = []
for _ in range(n):
    std = 0
    x, y = input().split()
    prices.append(int(x))
    titles.append(list(set(str(y))))

# print(prices)
# [ [],  [],  [] ]
divided_letters = [[] for i in range(len(target))]
for i in range(len(titles)):
    for j in range(len(target)):  # 0 1 2
        if target[j] in titles[i]:
            divided_letters[j].append(i)

# print(divided_letters)


pd = []
pd += product(*divided_letters)

min_price = int(1e9)
for case in pd:
    case = list(set(case))
    tmp = 0
    for i in case:
        tmp += prices[i]
    min_price = min(min_price, tmp)
    # print(case, min_price)


if min_price == int(1e9):
    print(-1)
else:
    print(min_price)
