def solution(lines):
    line_map = {}
    
    for start, end in lines:
        for i in range(start, end):
            line_map[i] = line_map.get(i, 0) + 1
            
    overlap_length = 0
    for count in line_map.values():
        if count >= 2:
            overlap_length += 1
            
    return overlap_length
    
    