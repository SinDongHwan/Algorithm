def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for idx, num in enumerate(num_list):
            if idx == 0:
                answer = num
            else:
                answer *= num
    return answer