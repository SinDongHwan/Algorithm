def solution(myString, pat):
    answer = 0
    pat = list(pat)
    for idx in range(len(pat)):
        if pat[idx] == 'A':
            pat[idx] = 'B'
        else:
            pat[idx] = 'A'
    pat = ''.join(pat)
    
    if myString.count(pat):
        answer = 1
    return answer