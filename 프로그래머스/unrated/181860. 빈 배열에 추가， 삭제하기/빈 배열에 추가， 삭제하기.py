def solution(arr, flag):
    answer = []
    for i, f in zip(arr,flag):
        if f:
            answer += [i] * i *2
        elif len(answer) != 0 and not f:
            del answer[-1*i:]
    return answer