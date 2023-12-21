def solution(picture, k):
    answer = []
    
    for col in picture:
        pixel = ''
        for row in col:
            pixel += row*k
        for i in range(k):
            answer.append(pixel)
    return answer