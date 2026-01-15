import math

def solution(n):
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return 1
    else:
        return 2