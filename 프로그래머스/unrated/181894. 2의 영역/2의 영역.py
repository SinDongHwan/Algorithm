def solution(arr):
    answer = []
    
    if arr.count(2) == 0:
        answer.append(-1)
    else:
        e = len(arr) - arr[::-1].index(2)
        answer += arr[arr.index(2):e]
        
    return answer