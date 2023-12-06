def solution(num, n):
    answer = 0
    if 2 > num or 100 < num:
        print(f"num value Error : {num}")
        return -1
    if 2 > n or 9 < n:
        print(f"n value Error : {n}")
        return -1
    
    if num % n == 0:
        answer = 1
    return answer