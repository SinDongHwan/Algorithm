def solution(picture, k):
    answer = []
    
    # for col in picture:
    #     pixel = ''
    #     for row in col:
    #         pixel += row*k
    #     for i in range(k):
    #         answer.append(pixel)
    
    for idx in range(len(picture)):
        for _ in range(k):
            answer.append(picture[idx].replace('.', '.'*k).replace('x', 'x'*k))
    return answer