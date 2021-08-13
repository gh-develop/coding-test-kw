import sys
sys.stdin = open('ex_093_input.txt', 'r')


num1 = [1,3,6,78,35,55]
num2 = [12,24,35,24,88,120,155]

interSection = [value for value in num1 for value2 in num2 if value == value2]
print(interSection)