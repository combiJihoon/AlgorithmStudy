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
