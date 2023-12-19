def solution(arr, k):
    answer = []
    set_arr = list(set(arr))
    i = 0
    while len(answer) < k:
        if len(answer) == 0:
            answer.append(arr[i])
        else:
            if i < len(arr) and arr[i] not in answer:
                answer.append(arr[i])
            elif -1 in answer:
                if len(answer[:answer.index(-1)]) == len(set_arr):
                    answer.append(-1)
            elif -1 not in answer:
                if len(answer) == len(set_arr):
                    answer.append(-1)

        i += 1
            
    return answer