def solution(num_list):
    answer = 0
    mul = 1
    pow_of_sum = 0

    if 2 > len(num_list) or 10 < len(num_list):
        print(f"num_list length Error : {len(num_list)}")
        return -1
    
    for i in num_list:
        mul *= i
    pow_of_sum = sum(num_list)**2

    if mul < pow_of_sum:
        answer = 1
        
    return answer