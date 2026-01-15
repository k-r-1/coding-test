def solution(my_string):
    lower_str = my_string.lower()
    result = sorted(lower_str)
    return "".join(result)