def binary_search(data, start, end, target):
    #끝나는 시점     
    if start > end:
        return False
    mid = (start + end)//2
    #찾고자 하는 값이 중간값과 일치하면 True를 리턴
    if data[mid] == target:
        return True
    #찾고자 하는 값이 중간값보다 작으면 중간값의 왼쪽 탐색
    elif data[mid] > target:
        return binary_search(data, start, mid-1, target)
    #찾고자 하는 값이 중간값보다 크면 중간값의 오른쪽 탐색
    else:
        return binary_search(data,mid+1,end,target)

n, target = map(int,input().split())
data = list(map(int, input().split()))

result = binary_search(data, 0, n-1, target)

if result:
    print("있습니다")
else:print("없습니다")