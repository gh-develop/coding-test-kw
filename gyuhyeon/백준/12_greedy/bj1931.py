import sys
sys.stdin = open('bj1931_in.txt', 'r')


def selector(acts):
    selected_act = 0
    ans = [selected_act]

    for act in range(1, len(acts)):
        if acts[act][0] >= acts[selected_act][1]:
            selected_act = act
            ans.append(selected_act)

    return len(ans)


n = int(input())
_acts = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    _acts.append((a, b))

_acts.sort(key=lambda x:(x[1], x[0]))
print(selector(_acts))