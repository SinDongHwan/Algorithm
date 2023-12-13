def solution(arr, queries):
    answer = []
    for (s, e) in queries:
        arr[s:e+1] = [num+1 for num in arr[s:e+1]]
    answer = arr
    return answer