def solution(arr):
    row = len(arr) # 행
    col = len(arr[0]) # 열
    
    if row > col:
        # 각 행의 끝에 0 추가
        for i in range(row):
            arr[i] += [0] * (row - col)
    elif col > row:
        # 각 열의 끝에 0을 추가
        for _ in range(col - row):
            arr.append([0] * col)
            
    return arr