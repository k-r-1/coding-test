def solution(ineq, eq, n, m):
    answer = 0
    condition = ineq + eq
    if condition == '>=' and n >= m:
        return 1
    elif condition == '<=' and n <= m:
        return 1
    elif condition == '>!' and n > m:
        return 1
    elif condition == '<!' and n < m:
        return 1
    else:
        return 0