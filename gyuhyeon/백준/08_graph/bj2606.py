from collections import deque
import sys
sys.stdin = open('bj2606_in.txt', 'r')


def breadth_first_search(graph, root):
    # sequence of visited nodes
    visited = []
    # nodes which are discovered & queued
    discovered = []
    queue = deque([root])
    discovered.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        visited.append(node)
        undiscovered = set(graph[node]).difference(set(discovered))

        if len(undiscovered) > 0:
            for elem in sorted(undiscovered):
                queue.append(elem)
                discovered.append(elem)

    return visited


size = int(input())
graph1 = [[] * size for i in range(size+1)]    # data: [[], [], [], []]
loop = int(input())
for _ in range(loop):
    n, m = map(int, input().split())
    graph1[n].append(m)
    graph1[m].append(n)


ans = breadth_first_search(graph1, 1)

print(len(ans)-1)
