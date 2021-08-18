class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,data):
        self.head = Node(data)
    def append(self, data):
        cur = self.head        #cur가 무엇을 가리키고 있는지 잘 봐야함
        while cur.next != None:#LinkField(next)가 비어있지 않을때까지
            cur = cur.next     #즉, 링크를타서 마지막 Node까지 접근을 의미함 
        cur.next = Node(data)  #마지막 Node에 도착해서 그 Node의 
                               #LinkField(cur.next)에 새로운 Node를 추가한다.
    def getNode(self,index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cur = cur.next
            cnt += 1
        return cur
    def delNode(self,index):
        cur = self.head
        if index == 0:           #맨 앞 Node를 삭제하는 경우
            self.head = cur.next #헤드에 다음놈을 할당
            return
        prevNode = self.getNode(index-1)  #prevNode에 없애고 싶은 Node의 앞Node를 할당
        prevNode.next = prevNode.next.next#없애고 싶은 Node의 앞Node와 뒷Node를 이어줌
    def insert(self, index, data):
        newNode = Node(data)#newNode에 추가할 Node를 할당 
        if index == 0:      #앞(head자리)에 삽입하는 경우
            newNode.next = self.head
            self.head = newNode
            return
        prevNode = self.getNode(index-1)#추가하고 싶은 자리의 앞 Node를 prevNode에 할당
        nextNode = prevNode.next#prevNode의 다음Node를 nextNode에 할당
        prevNode.next = newNode#prevNode LinkField에 newNode를 할당
        newNode.next = nextNode#newNode의 LinkField에 nextNode를 할당
                               #함으로서 index자리에 삽입됨
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
