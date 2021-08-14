s = input()
cnt = 0
for i in s:
    if 64 < ord(i) < 68 :
        cnt += 3
    elif 67 < ord(i) < 71:
        cnt += 4
    elif 70 < ord(i) < 74:
        cnt +=5
    elif 73 < ord(i) < 77:
        cnt += 6
    elif 76 < ord(i) < 80:
        cnt += 7
    elif 79 < ord(i) < 84:
        cnt += 8
    elif 83 < ord(i) < 87:
        cnt += 9
    else :cnt += 10
print(cnt)
