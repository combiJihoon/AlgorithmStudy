import sys

input = sys.stdin.readline

case = list(input().strip())


def get_formula(case):
    num_list = []
    operators = []
    num = ''
    for val in case:
        if val != '-' and val != '+':
            num += val
        else:
            num_list.append(int(num))
            operators.append(val)
            num = ''

    num_list.append(int(num))

    return num_list, operators


num_list, operators = get_formula(case)

result = num_list[0]
num_list.remove(result)

for i in range(len(num_list)):
    if operators[i] == '-':
        result -= sum(num_list[i:])
        break
    else:
        result += num_list[i]

print(result)


'''
아주 간결한 다른 사람의 풀이
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e[0] - sum(e[1:]))
# input().split('-') -> ['30', '20+40', '20']
# map(int, x.split('+')) -> [30], [20, 40], [20]
# sum(map(int, x.split('+'))) -> 30, 60, 20
'''
