def solution(arr):
    x = 0
    while True:
        nxt = []
        for n in arr:
            if n >= 50 and n % 2 == 0:
                nxt.append(n // 2)
            elif n < 50 and n % 2 == 1:
                nxt.append(n * 2 + 1)
            else:
                nxt.append(n)
        if arr == nxt:
            return x
        
        arr = nxt
        
        x += 1
                