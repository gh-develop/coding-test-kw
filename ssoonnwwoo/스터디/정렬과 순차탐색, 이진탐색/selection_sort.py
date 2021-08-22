def selection_sort(data):
    for i in range(len(data)-1):#range(4-1) = range(3)
        lowest = i
        for num in range(i+1, len(data)):#range(i+1, 4)
            if data[lowest] > data[num]:
                lowest = num
        data[i], data[lowest] = data[lowest], data[i]
        print(data)
    return data

selection_sort([9,3,2,1])