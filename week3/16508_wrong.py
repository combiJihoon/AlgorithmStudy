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
tmp_titles = []
for _ in range(n):
    std = 0
    x, y = input().split()
    prices.append(int(x))
    tmp_titles.append(list((str(y))))


titles = []
for tmp in tmp_titles:
    titles.append(set(tmp))


# [ [],  [],  [] ]
divided_letters = [[] for i in range(len(target))]
for i in range(len(titles)):
    for j in range(len(target)):  # 0 1 2
        if target[j] in titles[i]:
            divided_letters[j].append(i)


pd = []
pd += product(*divided_letters)


is_impossible = False
min_price = int(1e9)
for case in pd:
    for i in case:
        if len(case) > len(tmp_titles[i]):
            is_impossible = True
            break
    if is_impossible:
        break
    case = list(set(case))
    tmp = 0
    for i in case:
        tmp += prices[i]
    min_price = min(min_price, tmp)


if min_price == int(1e9) or is_impossible:
    print(-1)
else:
    print(min_price)
