def solution(a, b):
    a_odd = a % 2 == 1
    b_odd = b % 2 == 1
    
    if a_odd and b_odd:
        return a**2 + b**2
    elif a_odd or b_odd:
        return 2 * (a + b)
    else:
        return abs(a - b)