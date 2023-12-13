def solution(todo_list, finished):
    answer = []
    answer = [todo for todo, finish in zip(todo_list, finished) if not finish]
    return answer