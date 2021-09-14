import sys

input = sys.stdin.readline

# n: 숫자의 자리수, k: 지워야할 개수
n, k = map(int, input().split())
target = list(input())

stack = []  # 41
cnt = 0
for i in range(n):
    while cnt < k and stack and stack[-1] < target[i]:
        stack.pop()
        cnt += 1
    stack.append(target[i])

# 맨 앞자리 수보다 뒤의 수가 작은 경우 반례가 될 수 있음
# 반례 : 945에서 2개 제거
# 그렇게 되면 cnt는 0이 되기 때문에 아래의 코드로 예외처리
if cnt < k:
    idx = k - cnt
    stack = stack[:-idx]
print("".join(stack))
