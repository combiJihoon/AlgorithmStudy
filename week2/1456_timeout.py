import sys
import math

input = sys.stdin.readline


def isPrime(num):
    is_prime = False
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:  # i가 소수
        is_prime = True  # 소수임을 표시
        return is_prime


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

def is_almostPrime(a, b):
    result = 0
    # max_num = int(1e7)
    end = int(math.sqrt(b))
    for i in range(2, end+1):
        if isPrime(i):
            j = 2
            while True:
                if a <= i ** j <= b:
                    result += 1
                    j += 1
                else:
                    break

    return result


a, b = map(int, input().split())

print(is_almostPrime(a, b))

# 1 <= x <= 1000
# 소수: 2, 3, 5, 7, ...
#      4, 9, 25, 49, ....
