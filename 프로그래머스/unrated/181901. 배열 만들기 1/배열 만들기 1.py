def solution(n, k):
    answer = []
#    answer = [i for i in range(1,n+1) if i%k == 0]
    answer = [i for i in range(k,n+1,k)]
    return answer