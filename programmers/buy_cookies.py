def solution(cookie):
    max_cnt = 0

    for i in range(len(cookie)-1):
        l_sum, l_idx = cookie[i], i  # 왼쪽 기준점
        r_sum, r_idx = cookie[i+1], i+1  # 오른쪽 기준점
        while True:
            if l_sum == r_sum:
                max_cnt = max(max_cnt, l_sum)

            if l_idx > 0 and l_sum <= r_sum:
                l_idx -= 1
                l_sum += cookie[l_idx]
            elif r_idx < len(cookie) - 1 and l_sum >= r_sum:
                r_idx += 1
                r_sum += cookie[r_idx]
            else:
                break  # 위에 해당하는 경우가 아니면 다른 기준점을 찾는다

    return max_cnt


cookie = [1, 1, 2, 3]
print(solution(cookie))

'''
<다른사람 풀이>
from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer

'''
