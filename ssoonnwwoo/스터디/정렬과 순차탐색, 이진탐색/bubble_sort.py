def bubble_sort(data):
    for i in range(len(data)):#range(5) 0~4
        swap = 0
        for j in range(len(data) -1 - i):#range(4-i) --> range(4~0) 
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap+=1
        print(data)
        if swap == 0:
            break
    return data
bubble_sort([9,7,5,3,1])