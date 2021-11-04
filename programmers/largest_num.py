
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    print(numbers)
    return "".join([str(num) for num in numbers])


print(solution([3, 30, 34, 5, 9]))
