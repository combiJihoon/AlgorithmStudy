import sys

input = sys.stdin.readline

'''
위치와 숫자 동일 : 스트라이크
숫자만 동일 : 볼

해당 수일 때 조건을 만족하는 지 판별
'''


def cntStrike(a, b):
    cnt = 0
    for i in range(3):
        if a[i] == b[i]:
            cnt += 1
    return cnt


def cntBall(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i != j and a[i] == b[j]:
                cnt += 1
    return cnt


# Start
n = int(input())

cond = []
for _ in range(n):
    cond.append(list(map(int, input().split())))


result = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                num = str(i) + str(j) + str(k)
                cnt = 0
                for c in cond:
                    if cntStrike(num, str(c[0])) == c[1] and cntBall(num, str(c[0])) == c[2]:
                        cnt += 1
                if cnt == n:
                    result += 1

print(result)
