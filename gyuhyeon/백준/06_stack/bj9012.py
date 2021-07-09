import sys
sys.stdin = open('bj9012_in.txt', 'r')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size ==0:
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data


def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in '(':
            stack.push(ch)
        if ch in ')':
            last = stack.pop()
            if last == '(' and ch == ')':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True


tc = int(input())

for _ in range(tc):

    test = input()
    m = check_brackets(test)
    if m:
        print('YES')
    else:
        print('NO')