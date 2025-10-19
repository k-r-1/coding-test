def solution(str_list):
    for i, x in enumerate(str_list):
        if x == 'l':
            return str_list[:i]
        elif x == 'r':
            return str[i+1:]
    return []