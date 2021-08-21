def binary_search(data, start, end, target):
    while start<=end:
        mid = (start+end)//2
        if data[mid]==target:
            return True
        elif data[mid] >target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n, target = map(int,input().split())
data = list(map(int, input().split()))
result = binary_search(data, 0, n-1, target)

if result:
    print("있습니다")
else:print("없습니다")