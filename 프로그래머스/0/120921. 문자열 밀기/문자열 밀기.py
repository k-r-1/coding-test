def solution(A, B):
    n = len(A)
    
    for k in range(n):
        if A == B:
            return k
        
        A = A[-1] + A[:-1]
        
    return -1
    