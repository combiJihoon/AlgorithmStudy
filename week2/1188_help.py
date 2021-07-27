import sys

input = sys.stdin.readline

sausages, people = map(int, input().split())


def gcd(m, n):
    a = max(m, n)
    b = min(m, n)
    if a % b == 0:
        return b
    return gcd(b, a % b)


print(people - gcd(sausages, people))


'''
# 왜 안댐...?
def solution(sausages, people):
    got_sausages = people // sausages
    no_sausages = people % sausages

    if no_sausages == 0:
        got_sausages -= 1
    else:
        if got_sausages == 0:
            cut = 0
            return cut
        else:
            no_sausages -= 1
    cut = (got_sausages + no_sausages) * sausages

    return cut


print(solution(sausages, people))
'''
