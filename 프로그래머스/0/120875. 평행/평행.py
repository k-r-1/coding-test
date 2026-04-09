def solution(dots):
    p1, p2, p3, p4 = dots
    
    get_slope = lambda pa, pb: (pb[1] - pa[1]) / (pb[0] - pa[0])
    
    # (p1, p2), (p3, p4)
    if get_slope(p1, p2) == get_slope(p3, p4):
        return 1
    # (p1, p3), (p2, p4)
    if get_slope(p1, p3) == get_slope(p2, p4):
        return 1
    # (p1, p4), (p2, p3)
    if get_slope(p1, p4) == get_slope(p2, p3):
        return 1
    
    return 0
    
    
    
    
    