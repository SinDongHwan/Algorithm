def solution(num_list):
    answer = 0
    odd_sum = sum([num for idx, num in enumerate(num_list) if (idx+1)%2])
    even_sum = sum([num for idx, num in enumerate(num_list) if (idx+1)%2==0])
    answer = max(odd_sum, even_sum)
    return answer