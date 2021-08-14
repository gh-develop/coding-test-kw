import sys
input = sys.stdin.readline

S = input()
alphabet = []

for i in range(97,123):
    alphabet.append(S.find(chr(i)))

for i in alphabet:
    print(i, end = ' ')
    