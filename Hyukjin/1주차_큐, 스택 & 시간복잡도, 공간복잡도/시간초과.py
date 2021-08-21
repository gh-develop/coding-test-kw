import math

C = int(input())
INF = 1e8


def const(n, t, l):
    if l * INF >= n * t:
        print("May Pass.")
    else:
        print("TLE!")


def exp(n, t, l):
    calc = t * (2 << n)
    
    if calc <= l * INF:
        print("May Pass.")
    else:
        print("TLE!")


def fact(n, t, l):
    if n > 400000:
        print("TLE!")
    else:
        calc = t * math.factorial(n)

        if calc > l * INF:
            print("TLE!")
        else:
            print("May Pass.")
    


def square(n, t, l):
    if l * INF >= (n ** 2) * t:
        print("May Pass.")
    else:
        print("TLE!")


def cubic(n, t, l):
    if l * INF >= (n ** 3) * t:
        print("May Pass.")
    else:
        print("TLE!")


for test_case in range(1, C + 1):
    s, n, t, l = map(str, input().split())
    n, t, l = int(n), int(t), int(l)

    if s == 'O(N)':
        const(n, t, l)
    elif s == 'O(N^2)':
        square(n, t, l)
    elif s == 'O(N^3)':
        cubic(n, t, l)
    elif s == 'O(2^N)':
        exp(n, t, l)
    elif s == 'O(N!)':
        fact(n, t, l)

