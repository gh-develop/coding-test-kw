class Stack(list):
    push = list.append
    pop = list.pop

    def is_empty(self):# 비었는지 있는지
        if not self:
            print("False")
            return False
        else:
            print("True")
            return True
    
    def peek(self):# 마지막 값 뭔지
        if not self.is_empty():
            return list[-1]
        else:
            print("UnderFlow")
            return