def solution(arr, n):
    answer = []
    answer = arr
    if len(answer)%2:
        for idx in range(0,len(answer),2):
            answer[idx] += n
    else:
        for idx in range(1,len(answer),2):
            answer[idx] += n
    return answer