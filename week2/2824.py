# import sys

# input = sys.stdin.readline


def gcd(n, m):
    big = max(n, m)
    small = min(n, m)
    if big % small == 0:
        return small
    return gcd(small, big % small)


# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# # n_list.sort()
# # m_list.sort()

# result = 1
# for i in range(len(n_list)):
#     for j in range(len(m_list)):
#         num1 = n_list[i]
#         num2 = m_list[j]
#         result *= gcd(num1, num2)

# # if len(str(result)) > 9:
# #     print(str(result)[-9:])
# # else:
# #     print(result)

# print(result)

# 18 8 4 = 320
# 4 9 6 = 108

# (2, 3^2)(2^3)(2^2) -> [0, 0, 5, 2] =>
# (2^2)(3^2)(2 3) -> [0, 0, 4, 3] => 2 ** 4 * 3** 2

print(gcd(3, 9))
