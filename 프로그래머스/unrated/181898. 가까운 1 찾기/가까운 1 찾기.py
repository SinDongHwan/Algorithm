def solution(arr, idx):
    answer = 0
#     if arr[idx:].count(1) == 0:
#         answer = -1
#     else:
#         answer = arr[idx:].index(1) + len(arr[:idx])
        
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
        
    return answer