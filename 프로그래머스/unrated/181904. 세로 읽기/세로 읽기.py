def solution(my_string, m, c):
    answer = ''
    answer = "".join([my_string[idx] for idx in range(c-1,len(my_string),m)])

    return answer