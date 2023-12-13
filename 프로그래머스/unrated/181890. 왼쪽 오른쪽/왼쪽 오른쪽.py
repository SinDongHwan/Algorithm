def solution(str_list):
    answer = []
    for idx, ch in enumerate(str_list):
        if ch == 'l':
            answer = str_list[:idx]
            break
        elif ch == 'r':
            answer = str_list[idx+1:]
            break
            
    return answer