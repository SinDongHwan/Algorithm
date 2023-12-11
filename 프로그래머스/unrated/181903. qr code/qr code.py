def solution(q, r, code):
    answer = ''
    # answer = "".join([code[idx] for idx in range(len(code)) if (idx%q)==r])
    answer = code[r::q] # idx*q+r == 0. r번째부터 q씩 증가
    return answer