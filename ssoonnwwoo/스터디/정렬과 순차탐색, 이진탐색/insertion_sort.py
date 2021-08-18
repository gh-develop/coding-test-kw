def insertion_sort(data):
    for i in range(len(data)):
        key = data[i]
        for num in range(i, 0, -1):
            if key < data[num-1]:
                data[num-1], data[num] = data[num], data[num-1]
            else:
                break
        print(data)
    return data

insertion_sort([9,3,2,5])