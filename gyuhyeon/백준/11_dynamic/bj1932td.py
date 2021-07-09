import sys
sys.stdin = open('bj1932_in.txt', 'r')



def max_path(row, col):
    if row == _size - 1:
        return _triangle[row][col]

    if _memo[row][col] == 0:
        path_left = _triangle[row][col] + max_path(row+1, col)
        path_right = _triangle[row][col] + max_path(row+1, col+1)
        _memo[row][col] = max(path_left, path_right)

    return _memo[row][col]


_triangle = []
_size = int(input())
_memo = [[0]*_size for j in range(_size)]

for _ in range(_size):
    _triangle.append(list(map(int, input().split())))

print(max_path(0, 0))
