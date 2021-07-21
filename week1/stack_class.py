import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if self.size() == 0:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        return self.stack[-1]


stack = Stack()

n = int(input())

for _ in range(n):
    func = input().split()
    if func[0] == 'push':
        stack.push(func[1])
    if func[0] == 'pop':
        print(stack.pop())
    if func[0] == 'size':
        print(stack.size())
    if func[0] == 'empty':
        print(stack.empty())
    if func[0] == 'top':
        print(stack.top())
