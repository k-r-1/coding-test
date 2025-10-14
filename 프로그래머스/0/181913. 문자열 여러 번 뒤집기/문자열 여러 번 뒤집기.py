def solution(my_string, queries):
    list_string = list(my_string)
    
    for s, e in queries:
        list_string[s:e+1] = reversed(list_string[s:e+1])
    return ''.join(list_string)