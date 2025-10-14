def solution(q, r, code):
    result = []
    for idx in range(len(code)):
        if r == idx % q:
            result.append(code[idx])
    return ''.join(result)