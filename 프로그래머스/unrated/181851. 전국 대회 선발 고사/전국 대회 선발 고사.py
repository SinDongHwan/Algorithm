def solution(rank, attendance):
    answer = 0
    rank_dict = dict()
    for i, (rank_, attend) in enumerate(zip(rank, attendance)):
        if attend:
            rank_dict[rank_] = i
    rank_dict = sorted(rank_dict.items())[:3]
    answer = 10000 * rank_dict[0][1] + 100 * rank_dict[1][1] + rank_dict[2][1]
    return answer