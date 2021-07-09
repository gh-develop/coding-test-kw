import bisect
import sys
sys.stdin = open('bj1920_in.txt', 'r')


def binary_search(ordered_list, target):
    index = bisect.bisect_left(ordered_list, target)

    if index < len(ordered_list) and ordered_list[index] == target:
        return 1
    else:
        return 0


n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
_target = list(map(int, input().split()))
_result = []

for i in range(m):
    _result.append(binary_search(card, _target[i]))
    print(_result[i])
