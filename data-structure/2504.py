import sys

input = sys.stdin.readline
string = input().strip()

stack = []
for i in string:
    if i == ')':
        tmp = 0
        while stack:
            x = stack.pop()
            if x == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            elif x == '[':
                print(0)
                sys.exit()
            else:
                if tmp == 0:
                    tmp = int(x)
                else:
                    tmp += int(x)

    elif i == ']':
        tmp = 0
        while stack:
            x = stack.pop()
            if x == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            elif x == '(':
                print(0)
                sys.exit()
            else:
                if tmp == 0:
                    tmp = int(x)
                else:
                    tmp += int(x)

    else:
        stack.append(i)

ans = 0
for i in stack:
    if i == '(' or i == '[':
        print(0)
        sys.exit()
    else:
        ans += i

print(ans)
