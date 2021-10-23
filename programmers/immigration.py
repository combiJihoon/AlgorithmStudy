'''
전체 로직은 주어진 심사대와 주어진 인원 수에서 가장 오래 걸리는 
최악의 심사 시간을 max로 두고, 시간을 이진 탐색 하면서 
현재 탐색하는 시간(mid)동안 심사가 가능한지 판단한다.
이는 해당 시간의 인원이 가능한 지를 통해 판단하며
만약 예상이 실제보다 더 크다면 적은 시간 탐색,
그렇지 않다면 더 큰 시간 탐색을 한다.
'''


def solution(n, times):
    s = 1  # 최소 1분 이상
    e = max(times) * n  # 모두가 가장 오래 걸리는 심사대로 간 경우(최대시간)
    while s < e:
        mid = (s + e) // 2  # 현재 가능한 전체 시간
        tot_ppl = 0

        for time in times:
            tot_ppl += mid // time

        if tot_ppl >= n:  # 가능한 인원이 n 이상인 경우
            e = mid
        else:
            s = mid + 1

    return e


n = 6
times = [7, 10]
print(solution(n, times))
