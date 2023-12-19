def solution(arr, n):
    answer = []
    for idx, num in enumerate(arr):
        if len(arr)%2 and idx%2 == 0:
            arr[idx] += n
        elif len(arr)%2 == 0 and idx%2:
            arr[idx] += n
    answer = arr
    return answer