import sys
sys.stdin = open('bj1427_in.txt', 'r')

num = input()

# string->list
num = [int(val) for val in num]

# sorting
# num.sort(reverse=True)
#
# for item in num:
#     print(item, end="")

# another possible answer
# bubble sort
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j] >= num[j+1]:
            continue
        else:
            tmp = num[j+1]
            num[j+1] = num[j]
            num[j] = tmp

for item in num:
    print(item, end="")

# insertion sort
