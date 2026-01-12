def solution(s):
    s = list(s)
    result = []
    for ch in s:
        if s.count(ch) == 1:
            result.append(ch)
            
    return "".join(sorted(result))