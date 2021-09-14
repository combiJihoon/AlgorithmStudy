import sys

input = sys.stdin.readline

n = int(input())
limits = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if boxes[0] > limits[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        cnt += 1
        for i in range(n):
            if not boxes:
                break
            else:
                for j in range(len(boxes)):
                    if boxes[j] <= limits[i]:
                        boxes.pop(j)
                        break

    print(cnt)
