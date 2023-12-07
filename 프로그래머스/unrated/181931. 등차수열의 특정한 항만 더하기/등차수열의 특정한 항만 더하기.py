def solution(a, d, included):
    answer = 0
    if 1 > a or 100 < a:
        print(f"a value Error : {a}")
        return -1
    if 1 > d or 100 < d:
        print(f"b value Error : {b}")
        return -1
    if 1 > len(included) or 1 < len(included):
        print(f"included length Error : {len(included)}")
    
    answer = sum([a+(idx*d) for idx in range(len(included)) if included[idx]])
    
    return answer