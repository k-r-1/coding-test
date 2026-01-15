def solution(n):
    str_n = str(n)
    result = 0
    for i in str_n:
        result += int(i)
    return result