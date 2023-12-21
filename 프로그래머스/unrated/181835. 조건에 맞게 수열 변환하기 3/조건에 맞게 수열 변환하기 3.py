def solution(arr, k):
    answer = []
    answer = [num * k for num in arr] if k%2 else [num + k for num in arr]
    return answer