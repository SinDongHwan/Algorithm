def solution(number, n, m):
    answer = 0
    if 10 > number or 100 < number:
        print(f"number value Error : {number}")
        return -1
    if 2 > n or 10 < n:
        print(f"n value Error : {n}")
        return -1
    if 2 > m or 10 < m:
        print(f"m value Error : {m}")
    
    if (number % n) == 0 and (number % m) == 0:
        answer = 1
    
    return answer