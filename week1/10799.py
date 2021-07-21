import sys

input = sys.stdin.readline

case = input().strip()

stack = []
result = 0

for i in range(len(case)):
    if case[i] == '(':
        stack.append('(')
    else:
        # lazor인 경우
        if case[i-1] == '(':
            stack.pop()
            # stack에 남아 있는 '(' 개수만큼 더하기
            result += len(stack)
        # lazor가 아닌 경우 +1
        else:
            stack.pop()
            result += 1

print(result)
