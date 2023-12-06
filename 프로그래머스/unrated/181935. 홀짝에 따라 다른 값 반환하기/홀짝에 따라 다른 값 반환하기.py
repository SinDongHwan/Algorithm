def solution(n):
    answer = 0
    if n < 1 or 100 < n:
        print(f"n value Error : {n}")
        return -1
    if n % 2:
        answer = sum([n for n in range(n+1) if n%2])
    else:
        answer = sum([n**2 for n in range(n+1) if not(n%2)])
    return answer