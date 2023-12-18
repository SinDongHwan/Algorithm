def solution(myString):
    answer = []
    answer = sorted([word for word in myString.split('x') if word != ""])
    return answer