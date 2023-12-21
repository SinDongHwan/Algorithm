def solution(myString):
    answer = ''
    # for alpha in myString:
    #     answer += 'l' if alpha < 'l' else alpha
    answer = "".join(['l' if alpha < 'l' else alpha for alpha in myString])  
    return answer