def solution(my_string, k):
    answer = ''
    if 1 > len(my_string) or 100 < len(my_string):
        print(f"my_string length Error : {len(my_string)}")
        return -1
    if 1 > k or 100 < k:
        print(f"k value Error : {k}")
        return -1
    answer = my_string * k
    return answer