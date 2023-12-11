def solution(my_string, m, c):
    answer = ''
    # answer = "".join([my_string[idx] for idx in range(c-1,len(my_string),m)])
    answer = my_string[c-1::m] # c-1 ~ len(my_string), m번째 것만 추출
    return answer