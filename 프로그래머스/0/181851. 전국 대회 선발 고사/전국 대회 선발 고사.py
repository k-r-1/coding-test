def solution(rank, attendance):
    candidates = []
    
    for i in range(len(rank)):
        if attendance[i]:
            candidates.append((rank[i], i)) # 등수, 학생 번호 
    
    candidates.sort()
    
    a = candidates[0][1]
    b = candidates[1][1]
    c = candidates[2][1]
    
    return 10000 * a + 100 * b + c
    
                              
                           
                              
    