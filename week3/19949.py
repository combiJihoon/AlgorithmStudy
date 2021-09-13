# pypy3로 해야 통과(pypy3는 python보다 메모리 사용량이 더 많다.)

import sys

input = sys.stdin.readline
answers = list(map(int, input().split()))


def isAboveFive():
    score = 0
    # stack에 추가한 값이 answer과 동일하면 score + 1
    for i in range(10):
        if answers[i] == stack[i]:
            score += 1
            if score >= 5:
                return True
    return False


result = 0
stack = []


def dfs():
    global result

    if len(stack) == 10:
        if isAboveFive():
            result += 1
        return

    for i in range(1, 6):
        if len(stack) >= 2:
            if stack[-2] == stack[-1] == i:
                continue
        stack.append(i)
        dfs()
        stack.pop()


dfs()
print(result)


'''
백트래킹 다른 풀이



ans = [int(i) for i in input().split()]
dp = [
    [[[-1 for s in range(11)] for p2 in range(6)] for p1 in range(6)] for n in range(11)
]

def backTracking(n, p1, p2, score):
    if dp[n][p1][p2][score] != -1:
        return dp[n][p1][p2][score]

    if n == 10:
        if score >= 5:
            return 1
        else:
            return 0

    res = 0
    for i in range(1, 6):
        if p1 == p2 and p2 == i:
            pass
        elif ans[n] == i:
            res += backTracking(n + 1, p2, i, score + 1)
        else:
            res += backTracking(n + 1, p2, i, score)

    dp[n][p1][p2][score] = res
    return res
'''
