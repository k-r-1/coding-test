def solution(todo_list, finished):
    result = []
    return [ t for t, f in zip(todo_list, finished) if not f ]
           