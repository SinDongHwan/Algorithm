def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
        else:
            if answer[-1] == arr[i]:
                del answer[-1]
            else:
                answer.append(arr[i])
        i += 1
    if len(answer) == 0:
        answer.append(-1)
    return answer