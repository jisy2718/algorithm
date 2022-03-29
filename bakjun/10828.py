class stack():
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, num):
        self.stack.append(num)
        self.top += 1

    def pop(self):
        if self.stack:
            print(self.stack.pop())
            self.top -= 1
        else:
            print(-1)

    def size(self):
        print(self.top + 1)

    def empty(self):
        if self.top >= 0:
            print(0)
        else:
            print(1)

    def top(self):
        if self.top == -1:
            print(-1)
        else:
            print(self.stack[-1])


stack = stack()

N = int(input())
for _ in range(N):
    cur_input = input().split()
    # push 경우
    if cur_input[0] == 'push':
        stack.push(cur_input[1])

    # pop 경우
    elif cur_input[0] == 'pop':
        stack.pop()

    # size 경우
    elif cur_input[0] == 'size':
        stack.size()
    # empty 경우
    elif cur_input[0] == 'empty':
        stack.empty()
    # top 경우
    else:
        stack.top



