'''
풀이참고
https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EC%96%91%ED%8C%94%EC%A0%80%EC%9A%B8Python%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
'''
import sys

input = sys.stdin.readline

k = int(input())
weights = list(map(int, input().split()))
s = sum(weights)


def dfs(l, total):
    global s
    global result

    # s를 넘어가면 끝
    if total > s:
        return

    if l == k:
        if 1 <= total <= s:
            result.add(total)
    else:
        # l이 n이 되기 전까지 더하기, 빼기, 그대로 반복
        dfs(l+1, total+weights[l])
        dfs(l+1, total-weights[l])
        dfs(l+1, total)


result = set()
dfs(0, 0)
print(s-len(result))
