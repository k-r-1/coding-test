def solution(l, r):
    # l <= i <= r
    # 0 or 5 -> 오름차순
    arr = []
    for i in range(l, r+1):
        s = str(i)
        if all(ch in ['0', '5'] for ch in s):
            arr.append(i)
    arr.sort()
    return arr if arr else [-1]