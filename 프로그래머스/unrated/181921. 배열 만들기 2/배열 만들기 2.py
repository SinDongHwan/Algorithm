def solution(l, r):
    answer = []
    if l < 1 or l > 1000000:
        print(f"l value Error : {l}")
        return -1
    if  r < 1 or r > 1000000:
        print(f"r value Error : {r}")
        return -1
    
    for val in range(l, r+1):
        if len(set(str(val)) - {'0', '5'}) == 0:
            answer.append(val)
    answer = answer if len(answer) else [-1]
    return answer