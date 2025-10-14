def solution(my_string, indices):
    return ''.join([ch for idx, ch in enumerate(my_string) if idx not in indices])