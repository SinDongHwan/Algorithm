def solution(n):
    answer = [[]]
    # for i in range(n):
    #     if len(answer) == i :
    #         answer.append([])
    #     for j in range(n):
    #         if i == j:
    #             answer[i].append(1)
    #         else:
    #             answer[i].append(0)
    
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer