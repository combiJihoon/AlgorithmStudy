import sys

input = sys.stdin.readline

n = int(input())

if n in [1, 3]:
    print(-1)
elif (n % 5) % 2 == 0:
    print((n // 5) + ((n % 5) // 2))
else:
    print(((n // 5) - 1) + ((n % 5) + 5) // 2)

'''
괜찮은 다른 풀이
n = int(input())

count = 0

while n > 0:
    if n % 5 == 0:
        print(n // 5 + count)
        break

    n -= 2
    count += 1

if n < 0:
    print('-1')

'''
