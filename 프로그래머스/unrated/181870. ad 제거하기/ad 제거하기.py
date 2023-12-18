def solution(strArr):
    answer = []
    answer = [word for word in strArr if 'ad' not in word]
    return answer