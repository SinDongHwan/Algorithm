def solution(arr):
    answer = 0
    changed = True
    while changed:
        changed = False
        for idx, element in enumerate(arr):
            if element >= 50 and element%2 == 0:
                arr[idx] = arr[idx] // 2
                changed += True
            elif element < 50 and element%2:
                arr[idx] = arr[idx] * 2 + 1
                changed += True
                
        answer = answer + 1 if changed else answer
        
    return answer