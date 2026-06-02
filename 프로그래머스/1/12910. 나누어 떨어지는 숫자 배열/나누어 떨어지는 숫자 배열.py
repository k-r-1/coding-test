def solution(arr, divisor):
    answer = [e for e in arr if e % divisor == 0]
    
    if not answer:
        answer = [-1]
    else:
        answer.sort()
        
    return answer
    