import sys

input = sys.stdin.readline
# 1~n까지, 길이가 m인 수열
n, m = map(int, input().split())

# 풀이 참조 : https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/
stack = []


def dfs():
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in range(1, n+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()


dfs()


'''
# 시간초과

min_num = 10 ** (m-1)
max_num = (10 ** (m-1)) * (n+1)
cond = [str(i) for i in range(1, n+1)]

for num in range(min_num, max_num+1):
    tmp = list(set(str(num)))
    # 중복 없음
    if len(tmp) == m:
        is_right = True
        for i in tmp:
            if int(i) > n or int(i) < 1:
                is_right = False
                break
        if is_right:
            print(" ".join(str(num)))
'''
