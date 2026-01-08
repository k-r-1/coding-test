def solution(n):
    fact = 1
    i = 1
    
    while fact <= n:
        i += 1
        fact *= i
        
    return i - 1
        