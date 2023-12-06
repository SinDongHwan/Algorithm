def solution(str1, str2):
    answer = ''
    if 1 > len(str1) or 10 < len(str1):
        print(f"str1 length Error : {len(str1)}")
    if 1 > len(str2) or 10 < len(str2):
        print(f"str2 length Error : {len(str2)}")
        
    for ch1, ch2 in zip(str1, str2):
        answer += ch1
        answer += ch2
        
    return answer