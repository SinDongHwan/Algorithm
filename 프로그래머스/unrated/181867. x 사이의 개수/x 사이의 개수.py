def solution(myString):
    answer = []
    answer = [len(word) for word in myString.split('x')]
    return answer