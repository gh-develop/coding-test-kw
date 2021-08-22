def insertion_sort(list):
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else:
                break
    return list

print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))