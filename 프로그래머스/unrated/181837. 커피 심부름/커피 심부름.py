def solution(order):
    answer = 0
    # for order_ in order:
    #     if ("americano" in order_) or ("anything" in order_):
    #         answer += 4500
    #     elif "cafelatte" in order_:
    #         answer += 5000
    
    for order_ in order:
        if "cafelatte" in order_:
            answer += 5000
        else:
            answer += 4500
    return answer