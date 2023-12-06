def solution(arr):
    answer = ''
    if 1 > len(arr) or 200 < len(arr):
        print(f"arr length Error: {len(arr)}")
        return -1
    answer = "".join(arr)
    return answer