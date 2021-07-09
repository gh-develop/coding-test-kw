import sys
sys.stdin = open('bj1932_in.txt', 'r')


def max_path(row, col):
    memo = [[0]*_size for _ in range(_size)]
    memo[-1] = _triangle[-1]

    for i in range(_size-2, -1, -1):
        for j in range(0, i+1):
            memo[i][j] = _triangle[i][j]+ max(memo[i+1][j], memo[i+1][j+1])

    return memo[row][col]


_triangle = []
_size = int(input())


for _ in range(_size):
    _triangle.append(list(map(int, input().split())))

print(max_path(0, 0))
