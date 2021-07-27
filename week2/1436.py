import sys

input = sys.stdin.readline

n = int(input())


# 1,     2    3     4     5      6
# 666, 1666, 2666, 3666, 4666, 5666, 7666, 8666, 9666, 10666,
# 11666, 12666, 13666, 14666, 15666, 17666,

# 10번째 찾기
# -> 6666이 나오면 건너뛴다.

'''
66, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664
6665, 6667,

1~ 10000 중에 666이 들어간 수
'''


def find_title(n):
    i = 666
    cnt = 0
    while True:
        target = str(i)
        if '666' in target:
            cnt += 1
            if cnt == n:
                break
        i += 1
    return i


print(find_title(n))
