def solution(score):
    # 영어, 수학 점수 score
    # score 평균 기준 등수 리턴 
    avg = []
    for eng, math in score:
        avg.append((eng + math) / 2)
        
    sorted_avg = sorted(avg, reverse=True)
    
    return [sorted_avg.index(i) + 1 for i in avg]