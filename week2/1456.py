'''
이유는 잘 모르겠는데, a <= (num**j) <= b로 탐색하면 안되고,
일단 b보다 작거나 같은 부분을 탐색한 후 a와 같거나 큰 쪽인 지를 탐색해야 한다.
아마 제곱승을 하면 숫자가 너무 커져서 그런 것 같다.
'''

import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())

# 소수 찾기
isprime_list = [True] * (int(math.sqrt(b))+1)
prime_list = []
for i in range(2, len(isprime_list)):
    if isprime_list[i]:
        for j in range(2*i, len(isprime_list), i):
            isprime_list[j] = False

prime_list = [i for i in range(2, len(isprime_list)) if isprime_list[i]]

# 거의 소수 찾기
result = 0
for num in prime_list:
    j = 2
    while True:
        if (num ** j) <= b:
            if (num ** j) >= a:
                result += 1
        else:
            break
        j += 1


print(result)
