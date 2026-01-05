def solution(age):
    table = "abcdefghij"
    return ''.join(table[int(ch)] for ch in str(age))
