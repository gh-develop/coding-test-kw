prices = [1, 2, 3, 2, 3]
# [5, 4, 1, 2, 1, 0]

def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 1
        if i == len(prices)-1:
            answer.append(0)
        else:
            for value in range(i+1, len(prices)-1):
                if prices[i] <= prices[value]:
                    count += 1
                else:
                    break
            answer.append(count)

    return answer

print(solution(prices))