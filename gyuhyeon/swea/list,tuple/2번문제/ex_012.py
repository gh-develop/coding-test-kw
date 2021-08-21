import sys
sys.stdin = open('2번문제/ex_012_input.txt', 'r')


problem = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
condition = 'aeiou'

ans2 = [value for value in problem if condition.count(value) == 0]
print(''.join(ans2))
