class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)

        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1

        data = self.head.data
        self.head = self.head.next
        return data


n = int(input())
q = Queue()

for i in range(1, n+1):
    q.enqueue(i)

while q.size > 0:
    if q.size == 1:
        print(q.head.data)
        break

    q.dequeue()
    tmp = q.dequeue()
    q.enqueue(tmp)


