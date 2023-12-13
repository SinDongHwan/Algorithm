def solution(n, slicer, num_list):
    answer = []
    s, e, t = slicer
    
    if n == 1:
        answer = num_list[:e+1]
    elif n == 2:
        answer = num_list[s:]
    elif n == 3:
        answer = num_list[s:e+1]
    else:
        answer = num_list[s:e+1:t]
        
    return answer