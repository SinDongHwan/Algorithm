def solution(arr):
    answer = []
    i = 1
    while i < len(arr):
        i *= 2
    answer = arr + [0] * (i - len(arr)) if i > len(arr) else arr
    return answer