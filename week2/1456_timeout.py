import sys
import math

# def isPrime(num):
#     is_prime = False
#     cnt = 0
#     for i in range(2, num+1):
#         if num % i == 0:
#             cnt += 1
#             if cnt > 1:
#                 break
#     if cnt == 1:  # i가 소수
#         is_prime = True  # 소수임을 표시
#         return is_prime


# def is_almostPrime(a, b):
#     result = 0
#     # # a~b 사이 리스트
#     # range_list = [i for i in range(a, b+1)]
#     # 소수 후보 : 2부터 시작
#     end = int(math.sqrt(b))
#     for i in range(2, end+1):
#         if isPrime(i):
#             j = 2
#             while True:
#                 if i ** j <= b:
#                     result += 1
#                     j += 1
#                 else:
#                     break

#     return result

# def is_almostPrime(a, b):
#     max_num = int(1e7)
#     # 소수 체크
#     prime_list = [True] * (max_num+1)
#     for i in range(2, len(prime_list)):
#         if prime_list[i]:
#             for j in range(2, (max_num//i)+1):
#                 if prime_list[i * j]:
#                     prime_list[i * j] = False

#     result = 0
#     i = 2
#     for i in range(2, b+1):
#         if i ** 2 > b:
#             break
#         # 소수일 때 n제곱이 a, b 사이인지 확인
#         if prime_list[i]:
#             n = 2
#             while True:
#                 if a <= i ** n <= b:
#                     result += 1
#                 if i ** n > b:
#                     break
#                 n += 1

#     return result

# def is_almostPrime(a, b):


# 1 <= x <= 1000
# 소수: 2, 3, 5, 7, ...
#      4, 9, 25, 49, ....
# 소수가 아닌 것을 구하면 된다...

# 10^7 까지 소수인 지를 구한 다음
# 제곱한 것의 범위가 a <= x <= b인 지 확인

# 소수의 배수인 수를 구하면 된다.
# A <= B <= 10^14
# -> 소수는 10^7 보다 작음
# -> 10^7까지 소수를 구하고 제곱한 것이 안에 속하는지 확인
input = sys.stdin.readline

a, b = map(int, input().split())

# 소수 찾기
isprime_list = [True] * (math.sqrt(b)+1)
prime_list = []
for i in range(2, len(prime_list)):
    if isprime_list[i]:
        prime_list.append(i)
        j = i
        while j < len(prime_list):
            isprime_list[j] = False
            j += i

# 거의 소수 찾기

result = 0
for num in prime_list:
    j = 2
    while True:
        num **= j
        if a <= num:
            if num <= b:
                result += 1
            else:
                break
        else:
            j += 1

print(result)
