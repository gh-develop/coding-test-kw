import sys
a  = int(sys.stdin.readline())
cnt = 0
result = a
while True :
    b = result // 10
    c = result % 10
    d = (b + c)%10
    result = c*10+d
    cnt += 1
    if result == a:
        print(cnt)
        break