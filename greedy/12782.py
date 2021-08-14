import sys

input = sys.stdin.readline

n = int(input())

result = []
cnt = 0
while cnt < n:
    x, y = map(str, input().split())

    one = 0
    zero = 0
    for i in range(len(y)):
        if x[i] != y[i]:
            if y[i] == '0':
                zero += 1
            elif y[i] == '1':
                one += 1
    result.append(max(one, zero))
    cnt += 1

for r in result:
    print(r, end="\n")
