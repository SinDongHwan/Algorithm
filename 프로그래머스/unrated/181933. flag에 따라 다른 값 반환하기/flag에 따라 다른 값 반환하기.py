def solution(a, b, flag):
    answer = 0
    if a < -1000 or a > 1000:
        print(f"a value Error : {a}")
        return -1
    if b < -1000 or b > 1000:
        print(f"b value Error : {b}")
        return -1
    
    if flag:
        answer = a+b
    else:
        answer = a-b
    return answer