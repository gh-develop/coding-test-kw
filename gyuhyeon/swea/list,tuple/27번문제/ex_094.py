import sys
import copy
sys.stdin = open('ex_094_input.txt', 'r')


problem = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
problem2 = copy.deepcopy(problem)

# another possible answer
# ans2 = [item for item in [problem.pop(problem.index(value2)) if problem.count(value2) == problem2.count(value2) else problem.remove(value2) for value2 in problem2] if item is not None]

ans = [item for item in [problem.remove(value) if problem.count(value) > 1 else value for idx, value in enumerate(problem2)] if item is not None]
ans.sort()
print(ans)
