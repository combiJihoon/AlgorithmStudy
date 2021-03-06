# 유클리드 호제법
# https: // tech.lonpeach.com/2017/11/12/Euclidean-algorithm/

n, m = map(int, input().split())


def gcd(n, m):
    a = max(n, m)
    b = min(n, m)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def minMul(n, m):
    maxDivisor = gcd(n, m)
    return (n // maxDivisor) * (m // maxDivisor) * maxDivisor


print(gcd(n, m))
print(minMul(n, m))
