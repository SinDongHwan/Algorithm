def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for idx in indices:
        my_string.pop(idx)
        my_string.insert(idx, '0')
    answer = "".join(my_string).replace('0','')
    return answer