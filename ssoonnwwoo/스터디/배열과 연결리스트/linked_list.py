class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)
    def getNode(self,index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cur = cur.next
            cnt += 1
        return cur
    def delNode(self,index):
        cur = self.head
        if index == 0:
            self.head = cur.next
            return
        prevNode = self.getNode(index-1)
        prevNode.next = prevNode.next.next
    def insert(self, index, data):
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        prevNode = self.getNode(index-1)
        nextNode = prevNode.next
        prevNode.next = newNode
        newNode.next = nextNode
    def printList(self):
        cur = self.head
        print("[",end = '')
        while cur:
            print(cur.data,end = ', ')
            cur = cur.next
        print("]")

a = LinkedList(999)
a.append(1000)
a.append(1004)
a.insert(0,1)
a.insert(1,2)
a.insert(2,'...')
a.insert(3,998)
a.delNode(6)
a.printList()






