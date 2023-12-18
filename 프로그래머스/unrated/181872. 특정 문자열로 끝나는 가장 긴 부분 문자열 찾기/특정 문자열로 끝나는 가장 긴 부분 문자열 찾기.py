def solution(myString, pat):
    answer = ''
    last_index = myString[::-1].index(pat[::-1])
    answer = myString[:len(myString)-last_index]
    return answer