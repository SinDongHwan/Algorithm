def solution(my_string, index_list):
    answer = ''
    if len(my_string) < 1 or len(my_string) > 1000:
        print(f"my_string length Error: {len(my_string)}")
        return -1
    if len(index_list) < 1 or len(index_list) > 1000:
        print(f"index_list length Error : {len(index_list)}")
        return -1
    
    answer = "".join([my_string[index] for index in index_list])
    return answer