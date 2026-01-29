def solution(board):
    n = len(board)
    danger = [[False] * n for _ in range(n)]
    direction = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
         (1, -1), (1, 0), (1, 1)
    ]
    
    for i in range(n):
        for j in range(n):
            
            if board[i][j] == 1:
                for dx, dy in direction:
                    ni = i + dx
                    nj = j + dy
                    
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = True
    safe_count = 0                    
    for i in range(n):
        for j in range(n):
            if danger[i][j] == False:
                safe_count += 1
    return safe_count            
                