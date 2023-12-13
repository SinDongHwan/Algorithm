def solution(arr, query):
    answer = []
    for idx in range(len(query)):
        if idx % 2:
            arr = arr[query[idx]:]
        else:
            arr = arr[:query[idx]+1]
    answer = arr
    return answer