class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        pop_object = None
        if self.isEmpty():
            return pop_object
        else:
            pop_object = self.top.data
            self.top = self.top.next
            return pop_object

    def isEmpty(self):
        is_empty = False
        if self.top is None:
            is_empty = True
        return is_empty


def check_bracket(problem):
    stack = Stack()

    for idx in range(3):
        if idx == 0:
            for item in problem:
                if item == '(':
                    stack.push(item)
                if item == ')':
                    head = stack.pop()
                    if head == '(':
                        continue
                    else:
                        return False
        elif idx == 1:
            for item in problem:
                if item == '{':
                    stack.push(item)
                if item == '}':
                    head = stack.pop()
                    if head == '{':
                        continue
                    else:
                        return False

        elif idx == 2:
            for item in problem:
                if item == '[':
                    stack.push(item)
                if item == ']':
                    head = stack.pop()
                    if head == '[':
                        continue
                    else:
                        return False

    if stack.isEmpty():
        return True
    else:
        return False


problems = "({}[[]{})"

m = check_bracket(problems)
if m:
    print('YES')
else:
    print('NO')
