def solution(arr, k):
    if k % 2 == 1:
        return [k * x for x in arr]
    else:
        return [k + x for x in arr]