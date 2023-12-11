def solution(number):
    answer = 0
    if len(number) < 1 or len(number) > 100000:
        print(f"number value Error : {len(number)}")
        return -1
    number = int(number)

#    number = sum([int(num) for num in number])
    answer = number % 9
    return answer