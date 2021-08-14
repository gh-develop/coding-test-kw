n = int(input())
line = 0
a = 2
b = 0
while True:
    if n <= line:
        break
    line = sum(range(1, a))           #line += a     이렇게 했어도 될듯, b는 필요없고 ㅇㅇ
    a += 1
    b += 1

sub = line - n
if b % 2 == 0:
    print("%d/%d"%(b-sub, 1+sub))
else :
    print("%d/%d"%(1+sub, b-sub))