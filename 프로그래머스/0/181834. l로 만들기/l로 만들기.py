def solution(myString):
    result = []
    for ch in myString:
        if ch < 'l':
            result.append('l')
        else:
            result.append(ch)
    return ''.join(result)