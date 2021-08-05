import sys
import math
from itertools import combinations as cb

input = sys.stdin.readline
n, m = map(int, input().split())
weights = list(map(int, input().split()))


def isPrime(weight):
    if weight == 1:
        return False
    end = int(math.sqrt(weight))
    for i in range(2, end+1):
        if weight % i == 0:
            return False
    return True


cb_weights = [i for i in cb(weights, m)]

prime_weights = []
for weights in cb_weights:
    if isPrime(sum(weights)):
        prime_weights.append(sum(weights))

if prime_weights:
    print(*sorted(list(set(prime_weights))))
else:
    print(-1)
