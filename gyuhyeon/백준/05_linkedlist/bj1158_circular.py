class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prev_node, data):
        node = Node(data)
        self.size += 1

        # list is not empty
        if prev_node:
            node.next = prev_node.next
            prev_node.next = node

        # list is empty
        else:
            node.next = node
            self.head = node

    def traverse(self):
        current = self.head
        while True:
            yield current.data
            if current.next == self.head:
                break
            else:
                current = current.next

    def delete(self, prev_node):
        self.size -= 1

        # delete a non-head node
        if prev_node.next != self.head:
            prev_node.next = prev_node.next.next

        # delete the head node
        else:
            # multiple nodes in list
            if prev_node != self.head:
                self.head = self.head.next
                prev_node.next = self.head
            # only one node in list
            else:
                self.head = None


n, k = map(int, input().split())

jo = CircularList()
jo.insert(None, 1)
for i in range(n, 1, -1):
    jo.insert(jo.head, i)

print('<', end='')


if k == 1:
    for i in range(0, n):
        if i == n-1:
            print('{0}>'.format(jo.head.data), end='')
        else:
            print('{0}, '.format(jo.head.data), end='')
            jo.head = jo.head.next
else:
    while jo.size >= 1:
        if jo.size >= 2:
            target_prev = jo.head
            for hop in range(1, k):
                jo.head = jo.head.next
                if hop == k-2:
                    target_prev = jo.head
            print('{0}, '.format(jo.head.data), end='')
            jo.head = jo.head.next
            jo.delete(target_prev)
        else:
            print('{0}>'.format(jo.head.data), end='')
            break
