def solution(absolutes, signs):
    answer = 0
    
    for num, is_positive in zip(absolutes, signs):
        if is_positive:
            answer += num
        else:
            answer -= num
            
    return answer 