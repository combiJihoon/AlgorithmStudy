def digit_length(n):
    ans = 0
    # n은 0일 때 False이다.
    while n:
        # n을 10으로 나눈 몫만 취한다.
        n //= 10
        ans += 1
    return ans
