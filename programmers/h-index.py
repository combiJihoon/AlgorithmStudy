def solution(citations):
    n = len(citations)
    citations = sorted(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0


print(solution([1, 2, 3, 4]))
# [0, 1, 3, 5, 6]

# [1, 2, 3, 4]
# [2, 4, 6, 7]
# [3, 5, 6, 8, 9]
