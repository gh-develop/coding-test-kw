import sys
sys.stdin = open('bj17219_in.txt', 'r')

class Node:
    def __init__(self, data=None, num=None):
        self.data = data
        self.num = num
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, num):
        node = Node(data, num)
        parent = None
        current = self.root

        while current:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self.root = node
        elif node.data <= parent.data:
            parent.left = node
        else:
            parent.right = node

    def search(self, data):
        node = self.root
        while True:
            if node is None:
                return node
            elif node.data == data:
                return node.num
            elif data < node.data:
                node = node.left
            else:
                node = node.right


n, m = map(int, input().split())
name_list = [0]
tree = Tree()

for i in range(1, n+1):
    site, password = sys.stdin.readline().split()
    tree.insert(site, password)

for j in range(1, m+1):
    query = sys.stdin.readline().rstrip('\n')
    print(tree.search(query))
