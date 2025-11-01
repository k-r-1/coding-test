def solution(myString):
    parts = myString.split('x')
    arr = [s for s in parts if s != '']
    return sorted(arr)