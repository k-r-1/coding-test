def solution(arr):
    power = 1
    
    while power < len(arr):
        power *= 2
    
    while len(arr) < power:
        arr.append(0)
    
    return arr
    