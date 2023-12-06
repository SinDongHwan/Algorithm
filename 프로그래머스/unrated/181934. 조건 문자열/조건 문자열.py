def solution(ineq, eq, n, m):
    answer = 0
    if n < 1 or n > 100:
        print(f"n value Error : {n}")
        return -1
    if m < 1 or m > 100:
        print(f"m value Error : {m}")
        return -1
    
    eq = eq.replace("!","")
    if eval(f"{n}{ineq}{eq}{m}"):
        answer = 1
        
    return answer