def solution(num_list):
    answer = 0
    for idx, num in enumerate(num_list):
        while num_list[idx] != 1:
            if num_list[idx] % 2:
                num_list[idx] = (num_list[idx] - 1) // 2
            else:
                num_list[idx] = num_list[idx] // 2
            answer += 1
    return answer