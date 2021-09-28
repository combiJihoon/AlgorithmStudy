import sys

input = sys.stdin.readline
n, p = map(int, input().split())
d = {}
for _ in range(n):
    x, y = map(int, input().split())
    if str(x) not in d:
        d[str(x)] = [y]
    else:
        d[str(x)].append(y)

# stack[-1]보다 작은 값이 나오면 빼고 다음 값을 넣는다.
# 만약 stack[-1]과 같은 값이 나오면 넣지 않는다.
ans = 0
for key in d.keys():
    cnt = 0
    _list = d[key]
    stack = []
    for i in _list:
        if not stack:
            stack.append(i)
            cnt += 1
        else:
            if i == stack[-1]:
                continue
            elif i < stack[-1]:
                while stack:
                    if stack[-1] > i:
                        stack.pop()
                        cnt += 1
                    else:
                        break
                if (stack and stack[-1] != i) or (not stack):
                    stack.append(i)
                    cnt += 1
            else:
                stack.append(i)
                cnt += 1
    ans += cnt

print(ans)
