import sys

a,b,v = map(int,sys.stdin.readline().strip().split())

if (v-b)%(a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)