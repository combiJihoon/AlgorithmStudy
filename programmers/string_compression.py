def solution(s):
    ans = len(s)
    mid = (len(s) // 2) + 1

    for unit in range(1, mid):
        tmp = ''  # 압축된 문자열 저장
        prev = s[:unit]
        cnt = 1
        for i in range(unit, len(s), unit):
            if s[i:i+unit] == prev:
                cnt += 1
            else:
                if cnt >= 2:
                    tmp += str(cnt) + prev
                else:
                    tmp += prev
                prev = s[i:i+unit]
                cnt = 1
        if cnt >= 2:
            tmp += str(cnt) + prev
        else:
            tmp += prev
        ans = min(ans, len(tmp))
    return ans


# s1 = "aabbaccc"  # 7
# s2 = "ababcdcdababcdcd"  # 9
s3 = "abcabcdede"  # 8
print(solution(s3))
