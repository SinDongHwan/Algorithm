def solution(date1, date2):
    answer = 0
    if "".join(map(str, date1)).zfill(8) < "".join(map(str, date2)).zfill(8):
        answer = 1

    return answer