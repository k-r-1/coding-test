def solution(my_string, s, e):
    list_string = list(my_string)
    list_string[s:e+1] = reversed(my_string[s:e+1])
    return ''.join(list_string)