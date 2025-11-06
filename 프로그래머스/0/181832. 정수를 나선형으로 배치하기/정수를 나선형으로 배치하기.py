def solution(n):
    
    arr = [ n * [0] for _ in range(n) ]
    num = 1 
    
    top, bottom, left, right = 0, n - 1, 0, n - 1
    
    while num <= n * n:
        # 왼쪽 -> 오른쪽 방향으로 윗줄 채우기 
        for i in range(left, right + 1):
            arr[top][i] = num
            num += 1 
        top += 1
        
        # 위쪽 -> 아래쪽 방향으로 오른쪽열 채우기
        for i in range(top, bottom + 1):
            arr[i][right] = num
            num += 1
        right -= 1
        
        # 오른쪽 -> 왼쪽 방향으로 아랫줄 채우기
        for i in range(right, left - 1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1
        
        # 아래쪽 -> 위쪽 방향으로 왼쪽열 채우기 
        for i in range(bottom, top - 1, -1):
            arr[i][left] = num
            num += 1
        left += 1
        
    return arr