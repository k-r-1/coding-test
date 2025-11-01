def solution(myString):
    parts = myString.split('x')
    return [len(s) for s in parts]