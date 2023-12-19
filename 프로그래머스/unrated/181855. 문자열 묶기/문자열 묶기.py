def solution(strArr):
    answer = 0
    word_dict = dict()
    for word in strArr:
        if word_dict.get(len(word)) is None:
            word_dict[len(word)] = 1
        else:
            word_dict[len(word)] += 1
            
    answer = max(word_dict.values())
    return answer