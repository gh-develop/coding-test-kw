chr = input()
chr2hex = int(chr, 16)
for i in range(1, 16):
    result = chr2hex*i
    print('%X*%X=%X'%(chr2hex, i, result))