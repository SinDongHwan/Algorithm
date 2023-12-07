def solution(a, b, c):
    answer = 1

    if 1 > a or 6 < a:
        print(f"a value Error : {a}")
        return -1
    if 1 > b or 6 < b:
        print(f"b value Error : {b}")
        return -1
    if 1 > c or 6 < c:
        print(f"c value Error : {c}")
        return -1
    
#    cnt = 1
#    if a == b:
#        cnt += 1
#        if b == c:
#            cnt += 1
#    elif b == c or a == c:
#        cnt += 1
#
#    for i in range(1,cnt+1):
#        answer *= a**i+b**i+c**i
    cnt = 4 - len(set([a,b,c]))
    for i in range(1,cnt+1):
        answer *= a**i+b**i+c**i    
    return answer