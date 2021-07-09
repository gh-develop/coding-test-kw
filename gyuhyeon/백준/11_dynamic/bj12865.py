import sys
sys.stdin = open('bj12865_in.txt', 'r')


def knapsack(capacity, item):
    # capacity: current capacity
    # item: index of the item to
    # _number: number of items
    # _capacity: capacity of the knapsack
    # _weight: weight list of the items
    # _value: value list of the items

    if capacity == 0 or item >= _number:
        return 0

    if _weight[item] > capacity:
        return knapsack(capacity, item+1)

    if _memo.get((capacity,item)) is None:
        with_the_item = _value[item] + knapsack(capacity - _weight[item], item+1)
        without_the_item = knapsack(capacity, item+1)
        _memo[(capacity,item)] = max(with_the_item, without_the_item)

    return _memo[(capacity,item)]


_number, _capacity = map(int, input().split())
_weight = []
_value = []
_memo = {}

for i in range(_number):
    n, m = map(int, input().split())
    _weight.append(n)
    _value.append(m)

print(knapsack(_capacity, 0))
