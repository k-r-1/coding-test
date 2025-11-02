def solution(myString, pat):
    swap = ''
    for s in myString:
        if s == 'A':
            swap += 'B'
        elif s == 'B':
            swap += 'A'
            
    return 1 if pat in swap else 0
            