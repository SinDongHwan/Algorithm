def solution(str_list, ex):
    answer = ''
    answer = "".join([word for word in str_list if ex not in word])
    return answer