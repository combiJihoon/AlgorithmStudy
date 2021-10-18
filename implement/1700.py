import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
plug = [0] * n  # 안꽂혀 있으면 0
cnt = 0
idx = pos = ch_idx = 0
for i in arr:
    if i not in plug:
        if 0 in plug:
            # 0이 있는 자리에 꽂음
            plug[plug.index(0)] = i
        else:  # 전부 꽂혀있는 경우
            for j in plug:
                # 뒤에 동일한 것이 없다면 교체해 줘야 함
                if j not in arr[idx:]:
                    ch_idx = j
                    break
                elif arr[idx:].index(j) > pos:
                    ch_idx = j
                    pos = arr[idx:].index(j)
            plug[plug.index(ch_idx)] = i  # 플러그 교체
            ch_idx = pos = 0  # 원상 복구
            cnt += 1
    idx += 1
print(cnt)
