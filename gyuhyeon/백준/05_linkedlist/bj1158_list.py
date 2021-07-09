n, k = map(int, input().split())

jo = []
for i in range(1, n+1):
    jo.append(i)

print('<', end='')
index = 0

if k == 1:
    for i, value in enumerate(jo):
        if i == (len(jo)-1):
            print('{0}>'.format(value), end='')
        else:
            #print('{0}, '.format(value), end='')
            print(f'{value}, ', end='')
else:
    while len(jo) > 0:

        for _ in range(k-1):
            index += 1
            if index == len(jo):
                index = 0
        if len(jo) == 1:
            print('{0}>'.format(jo.pop(index)), end='')

        else:
            print('{0}, '.format(jo.pop(index)), end='')

        if index == len(jo):
            index = 0
