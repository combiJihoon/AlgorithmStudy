import sys
from collections import deque

input = sys.stdin.readline
q = deque()
cnt = 0

n = int(input())
for i in range(n):
    func = input().split()

    if func[0] == 'push':
        q.append(func[1])

    elif func[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif func[0] == 'size':
        print(len(q))

    elif func[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif func[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif func[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
