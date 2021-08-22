def binary_search(data, start, target):
    end = len(data) -1
#마지막 전 메서드에서 start, mid, end가 하나로 합쳐짐.
#메서드가 한번더 진행 되는데 검색 값이 없으면 (end는 그대로 start+1)이 되던가
#(start는 그대로 end -1)이 됨. 그래서 start가 end보다 커지므로 while문 탈출
    while start <= end:
        mid = start + (end - start)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
    return False

print(binary_search([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],0,1023))