import sys

input = sys.stdin.readline

num = str(input()).strip()
check = num

cnt = 0

while True:
    if len(num) == 1:
        temp_num = "0" + num
        num = temp_num
    else:
        temp_num = str(int(num[0]) + int(num[1]))
        if len(temp_num) == 1:
            temp_num = "0" + temp_num
    new_num = num[1] + temp_num[1]
    cnt += 1
    if check == str(int(new_num)):
        print(cnt)
        break
    else:
        num = new_num

# num[0] + num[1] = temp_num -> new_num
# 0 + 9 = 09 -> 99
# 9 + 9 = 18 -> 98
# 9 + 8 = 17 -> 87
# 8 + 7 = 15 -> 75
# 7 + 5 = 12 -> 52
# 5 + 2 = 7 -> 27
# 2 + 7 = 9
