def solution(strArr):
    length_count = {}
    for s in strArr:
        l = len(s)
        if l in length_count:
            length_count[l] += 1
        else:
            length_count[l] = 1
        
    return max(length_count.values())