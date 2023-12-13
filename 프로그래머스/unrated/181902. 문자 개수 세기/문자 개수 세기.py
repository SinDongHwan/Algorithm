def solution(my_string):
    answer = [0] * ((ord('Z') - ord('A') + 1) + (ord('z') - ord('a')+1)) 

    for string in my_string:
        if string.islower():
            answer[26+ord(string)-ord('a')] += 1
        else:
            answer[ord(string)-ord('A')] += 1

    return answer