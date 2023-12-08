def solution(start_num, end_num):
    answer = []
    if start_num < 0 or start_num > 50:
        print(f"start_num value Error : {start_num}")
        return -1
    if end_num < 0 or end_num > 50:
        print(f"end_num value Error : {end_num}")
        return -1
    
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer