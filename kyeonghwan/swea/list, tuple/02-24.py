list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
list3=[list1[i] for i in range(len(list1)) for j in range(len(list2)) if list1[i] == list2[j]]
print("{0}".format(list3))
