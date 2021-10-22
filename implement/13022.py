import sys
from itertools import permutations as pm

input = sys.stdin.readline
words = str(input().strip())

if words[0] != 'w' or words[-1] != 'f' or len(words) % 4 != 0:
    print(0)
    sys.exit()


def check():
    if count[0] == count[1] and count[1] == count[2] and count[2] == count[3]:
        return True
    return False


words = words.replace('w', "0")
words = words.replace('o', "1")
words = words.replace('l', "2")
words = words.replace('f', "3")

count = [0] * 4
count[0] = 1

# diff = -3이 되면 다음 w가 되며 한 사이클이 끝난 것
for i in range(1, len(words)):
    prev = int(words[i-1])
    cur = int(words[i])
    diff = cur - prev
    if diff == -3:
        if check():
            count = [0] * 4
            count[0] = 1
        else:
            print(0)
            sys.exit()
    else:
        if diff == 0 or diff == 1:  # 다음 글자와는 다르면 1, 같으면 0차이
            count[cur] += 1
        else:
            print(0)
            sys.exit()
if not check():
    print(0)
    sys.exit()
print(1)


'''
# wolf order: idx 0 = before, idx 1 = after
order = {
    'w': ['o', 0],
    'o': ['l', 0],
    'l': ['f', 0],
    'f': ['w', 0]
}

if words[0] != 'w' or words[-1] != 'f' or len(words) % 4 != 0:
    print(0)
    sys.exit()

order['w'][1] += 1
# 순서 판단
for i in range(1, len(words)):
    if words[i] != words[i-1] and words[i] != order[words[i-1]][0]:
        print(0)
        sys.exit()
    order[words[i]][1] += 1

# 개수 판단
val_arr = [val[1] for val in order.values()]
std = val_arr[0]
for val in val_arr[1:]:
    if std != val:
        print(0)
        sys.exit()
    std = val

print(1)
'''
