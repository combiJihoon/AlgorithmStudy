import sys
import math

input = sys.stdin.readline

n = int(input())

# 소수 판정
'''
시간초과
def isPrime(x):
    dp = [True] * 1005000
    dp[1] = False
    m = int(math.sqrt(1005000))
    for i in range(2, m+1):
        if dp[i]:
            for j in range(i+i, 1005000, i):
                dp[j] = False

    return dp[x]

def isPrime(x):
    dp = [True] * (x+1)
    dp[1] = False
    for i in range(2, x+1):
        if dp[i]:
            for j in range(i+i, x+1, i):
                dp[j] = False

    return dp[x]

'''

# 팰린드롬 판정
'''
틀린 코드
def isPalindrome(x):
    x = str(x)
    mid = len(x) // 2
    for i in range(mid):
        if x[i] == x[len(x)-i-1]:
            return True
        else:
            return False
'''


def isPrime(x):
    if x == 1:
        return False
    #
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def isPalindrome(x):
    x = str(x)
    tmp = x[::-1]
    if x == tmp:
        return True
    else:
        return False


def solution(n):
    while True:
        if isPalindrome(n) and isPrime(n):
            return n
        n += 1


print(solution(n))
