def solution(a, b, c, d):
    answer = 0
    if a < 1 or a > 6:
        print(f"a value Error : {a}")
        return -1
    if b < 1 or b > 6:
        print(f"b value Error : {b}")
        return -1
    if c < 1 or c > 6:
        print(f"c value Error : {c}")
        return -1
    if d < 1 or d > 6:
        print(f"d value Error : {d}")
        return -1
    
    num_list = list(set([a,b,c,d]))

    if len(num_list) == 1:
        answer = 1111 * num_list[0]
    elif len(num_list) == 2:
        if [a,b,c,d].count(num_list[0]) == 2:
            answer = (num_list[0]+num_list[1]) * abs(num_list[0]-num_list[1])
        elif [a,b,c,d].count(num_list[0]) == 3:
            answer = (10*num_list[0]+num_list[1]) ** 2
        elif [a,b,c,d].count(num_list[1]) == 3:
            answer = (10*num_list[1]+num_list[0]) ** 2
    elif len(set(num_list)) == 3:
        if [a,b,c,d].count(num_list[0]) == 2:
            answer = num_list[1] * num_list[2]
        elif [a,b,c,d].count(num_list[1]) == 2:
            answer = num_list[0] * num_list[2]
        elif [a,b,c,d].count(num_list[2]) == 2:
            answer = num_list[0] * num_list[1]
    elif len(num_list) == 4:
        answer = min([a,b,c,d])
        
        
    return answer