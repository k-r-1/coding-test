def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        sum_str = t[i: i + len(p)]
        if int(sum_str) <= int(p):
            answer += 1
            
    return answer
        