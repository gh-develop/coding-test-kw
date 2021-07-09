import copy
import sys
sys.stdin = open('bj10026_in.txt', 'r')


def depth_first_search(graph, row, col):
    stack = [(row, col)]
    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    color = graph[row][col]
    graph[row][col] = 'X'

    while len(stack) > 0:
        row, col = stack.pop()
        for m in range(4):
            next_row, next_col = row, col
            next_row += move[m][0]
            next_col += move[m][1]
            if not check_move(graph, next_row, next_col, color):
                continue

            stack.append((next_row, next_col))
            graph[next_row][next_col] = 'X'


def check_move(graph, row, col, color):
    if row < 0 or row >= size:
        return False
    if col < 0 or col >= size:
        return False
    if graph[row][col] != color:
        return False
    if graph[row][col] == 'X':
        return False

    return True


size = int(input())
graph2 = []
for i in range(size):
    tmp = list(input())
    graph2.append(tmp)

graph1 = copy.deepcopy(graph2)
graph0 = copy.deepcopy(graph2)
count1 = 0
count2 = 0
for i in range(size):
    for j in range(size):
        if graph1[i][j] == 'X':
            continue
        depth_first_search(graph1, i, j)

        count1 += 1

for i in range(size):
    for j in range(size):
        if graph0[i][j] == 'G':
            graph0[i][j] = 'R'


for i in range(size):
    for j in range(size):
        if graph0[i][j] == 'X':
            continue
        depth_first_search(graph0, i, j)

        count2 += 1

print(count1, count2)
