def solution(myString):
    answer = ''
    for alpha in myString:
        answer += 'l' if alpha < 'l' else alpha
        
    return answer