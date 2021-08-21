import sys
import math
sys.stdin = open('bj11332_in.txt', 'r')

# 그 다음 C개의 줄에는 시간 복잡도를 나타내는 문자열 S,
# 각 테스트 케이스마다 입력의 최대 범위 N, 테스트 케이스의 수를 나타내는 T랑 제한시간(초 단위) 를 나타내는 L이 주어진다.
# (1 <= C <= 100, 1 <= N <= 1000000, 1 <= T, L <= 10, N, T, L은 정수)

# S, N, T, L

# 1초에 100000000(10^8)가지 동작을 할 수 있다
# 1동작당 0.00000001초
# O (N)
# O (N^2)
# O (N^3)
# O (2^N)
# O (N!)

# O(N) 1000 10 10
# O(2^N) 1000 10 10
# O(N!) 2 10 10
# O(N^3) 1000 1 10
# O(N^3) 1001 1 10

#input case number
n = int(input()) # n = 5
# input data
str = [input().split() for _ in range(n)]

print(str)

# int(str[i][1])**3)*int(str[i][2]) <= int(str[i][3])*operation
# print((int(str[3][1])**3)*int(str[3][2]))
# print(type(int(str[3][3])*operation))

# 1초당 10^8동작
# 10초 10 * 10^8
# n = 5
for i in range(n):
    n, t, l = int(str[i][1]), int(str[i][2]), int(str[i][3])*100000000
    # 1000, 10, 10* 10^8-> 연산횟수
    # 'O(N)' -> 입력최대 1000개 10개 케이스가있다
    # 1: 1000, 2: 1000 3: 1000----- 10: 1000
    # 1000*10
    # 최대입력 1000
    # 'O(N)'-> 1000
    # 2n^2 + 20n
    # n^2
    # O(2^N) -> 2^1000
    # 2 ** n = 2^n
    # i = 0

    # n =10000000
    # 10000000!
    if str[i][0] == 'O(N)':
        if n * t <= l:
            print('May Pass.')
        else:
            print("TLE!")
    elif str[i][0] == 'O(2^N)':
        if (2 ** n) * t <= l:
            print('May Pass.')
        else:
            print("TLE!")
    elif str[i][0] == 'O(N!)':
        if math.factorial(n) * t <= l:
            print('May Pass.')
        else:
            print("TLE!")
    elif str[i][0] == 'O(N^3)':
        if (n ** 3) * t <= l:
            print('May Pass.')
        else:
            print("TLE!")
    elif str[i][0] == 'O(N^2)':
        if (n ** 2) * t <= l:
            print('May Pass.')
        else:
            print("TLE!")



