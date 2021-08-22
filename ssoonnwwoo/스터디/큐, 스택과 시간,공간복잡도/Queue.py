class Queue(list):
    enqueue = list.append
    
    def dequeue(self):
        data = self[0]
        del self[0]
        return data
    
    def is_empty(self):
        if not self:
            return True
        else:
            return False

list_queue = Queue()

list_queue.append(5)
list_queue.append(10)
list_queue.append(15)

print(list_queue.is_empty())

list_queue.dequeue()#5
print(list_queue)
list_queue.dequeue()#10
print(list_queue)
list_queue.dequeue()#15
print(list_queue.is_empty())

