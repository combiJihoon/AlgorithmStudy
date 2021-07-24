import sys

input = sys.stdin.readline

n = int(input())


result = 1
for i in range(2, n+1):
    result *= i
    result %= 100000000

    # 10으로 나눈 나머지가 0이면 몫만 남긴다.
    # 일의 자리 수 남기기
    while result % 10 == 0:
        result //= 10


print(result % 10)


'''
1 : 1 = 1
2 : 1 * 2 = 2
3 : 1 * 2 * 3 = 6
4 : 1 * 2 * 3 * 4 = 24 -> 4
5 : 1 * 2 * 3 * 4 * 5 = 120 -> 2 
6 : 1 * 2 * 3 * 4 * 5 * 6 = 720 -> 2
7 : 1 * 2 * 3 * 4 * 5 * 6 * 7 = ? -> 4
'''
