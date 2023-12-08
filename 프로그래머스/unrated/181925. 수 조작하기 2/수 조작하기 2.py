def solution(numLog):
    answer = ''
    if len(numLog) < 2 or len(numLog) > 100000:
        print(f"numLog length Error : {len(numLog)}")
        return -1
    
    wsda_dict = dict(zip([1,-1,10,-10],['w','s','d','a']))
    for idx, num in enumerate(numLog):
        if idx != 0:
            answer += wsda_dict[num - numLog[idx-1]]
    return answer