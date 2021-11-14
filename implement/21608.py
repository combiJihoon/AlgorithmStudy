import sys
from collections import defaultdict

input = sys.stdin.readline

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]


# 주변 자리 찾기
def dfs(x, y, case_list):
    unseated, likes = 0, 0
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if seated[nx][ny] == 0:
                unseated += 1
            if seated[nx][ny] in case_list:
                likes += 1
    return unseated, likes


n = int(input())
tot = n ** 2

seated = [[0] * n for _ in range(n)]
likes_dict = defaultdict(list)
for _ in range(tot):
    case_list = list(map(int, input().split()))
    likes_dict[case_list[0]] = case_list[1:]

    max_x, max_y = 0, 0
    max_likes, max_unseated = -1, -1
    for i in range(n):
        for j in range(n):
            if seated[i][j] == 0:
                unseated, likes = dfs(i, j, case_list)
                if (max_likes < likes) or (max_likes == likes and max_unseated < unseated):
                    max_x, max_y = i, j
                    max_likes = likes
                    max_unseated = unseated
    seated[max_x][max_y] = case_list[0]

satisfied = 0
for i in range(n):
    for j in range(n):
        student = seated[i][j]
        nearby_students = likes_dict[student]
        # 인접한 자리에 있는 학생들이 좋아하는 학생들인지 확인
        cnt = 0
        for dx, dy in moves:
            nx = i + dx
            ny = j + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if seated[nx][ny] in nearby_students:
                    cnt += 1
        # 점수 확인
        if cnt != 0:
            satisfied += 10 ** (cnt-1)


print(satisfied)
