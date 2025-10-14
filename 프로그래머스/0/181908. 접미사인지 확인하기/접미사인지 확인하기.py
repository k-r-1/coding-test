def solution(my_string, is_suffix):
    suffixes = [my_string[i:] for i in range(len(my_string))]
    return int(is_suffix in suffixes)