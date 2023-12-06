def solution(a, b):
    answer = 0
    if 1 > a or 10000 <= a:
        print(f"a value Error : {a}")
        return -1
    if 1 > b or 10000 <= b:
        print(f"b value Error : {b}")
        return -1
    
    answer = max(int(str(a)+str(b)), a*b*2)
    return answer