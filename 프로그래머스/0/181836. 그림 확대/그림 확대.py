def solution(picture, k):
    result = []
    for line in picture:
        expanded = ''.join(ch * k for ch in line)
        for _ in range(k):
            result.append(expanded)
    return result 