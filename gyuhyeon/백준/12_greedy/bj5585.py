import sys
sys.stdin = open('bj5585_in.txt', 'r')


def selector(change):
    count = 0
    while change > 0:
        if change >= 500:
            change -= 500
            count += 1
        elif change >= 100:
            change -= 100
            count += 1
        elif change >= 50:
            change -= 50
            count += 1
        elif change >= 10:
            change -= 10
            count += 1
        elif change >= 5:
            change -= 5
            count += 1
        else:
            change -= 1
            count += 1
    return count


n = int(input())
_change = 1000-n

print(selector(_change))
