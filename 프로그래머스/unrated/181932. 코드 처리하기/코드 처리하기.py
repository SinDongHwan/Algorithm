def solution(code):
    answer = ''
    mode = '0'
    if 1 > len(code) or 100000 < len(code):
        print(f"code length Error : {len(code)}")
        return -1

    for idx, ch in enumerate(code):
        if ch == '1':        
            mode = '0' if ch == mode else '1'
            continue
            
        if str(idx % 2) == mode:
            answer += ch
    
    answer = "EMPTY" if answer == '' else answer
        
    return answer