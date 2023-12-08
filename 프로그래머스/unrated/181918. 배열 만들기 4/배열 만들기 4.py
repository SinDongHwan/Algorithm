def solution(arr):
    stk = []
    if len(arr) < 1 or len(arr) > 100000:
        print(f"arr length Error : {len(arr)}")
        return -1
    
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk