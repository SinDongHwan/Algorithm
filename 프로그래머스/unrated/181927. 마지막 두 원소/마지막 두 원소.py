def solution(num_list):
    answer = []
    if 2 > len(num_list) or len(num_list) > 10 :
        print(f"num_list length Error : {len(num_list)}")
        return -1
    
#    for idx, num in enumerate(num_list):
#        answer.append(num)
#        
#        if idx == len(num_list)-1:
#            if num > num_list[idx-1]:
#                answer.append(num-num_list[idx-1])
#            else:
#                answer.append(num*2)
                
    if num_list[-2] < num_list[-1]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    answer = num_list
    return answer