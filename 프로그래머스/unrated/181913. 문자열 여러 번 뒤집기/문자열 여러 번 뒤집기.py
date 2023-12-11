def solution(my_string, queries):
    answer = ''
    if len(my_string) < 1 or len(my_string) > 1000:
        print(f"my_string length Error : {len(my_string)}")
        return -1
    if len(queries) < 1 or len(queries) > 1000:
        print(f"queries length Error: {len(queries)}")
        return -1
    
#    for s,e in queries:
#        reverse_string = my_string[s:e+1][::-1]
#        my_string = my_string[:s] + reverse_string + my_string[e+1:]
        
#    answer = my_string
    string_list = list(my_string)
    for s, e in queries:
        string_list[s:e+1] = string_list[s:e+1][::-1]
    answer = "".join(string_list)
    return answer