def solution(n, control):
    answer = 0
    if n < -100000 or n > 100000:
        print(f"n value Error : {n}")
        return -1
    if len(control) < 1 or len(control) > 100000:
        print(f"control length Error : {len(control)}")
        return -1
    
    for ct in control:
        if ct == 'w':
            n += 1
        elif ct == 's':
            n -= 1
        elif ct == 'd':
            n += 10
        else:
            n -= 10
    answer = n
    return answer