def solution(arr, queries):
    # [s, e, k] 
    # s<= i <= e
    # i > k 가장 작은 값 -> arr[i] 찾기
    result = []
    for q in queries:
        s, e, k = q[0], q[1], q[2]
        query = [arr[i] for i in range(s, e+1) if arr[i] > k]
        if query:
            result.append(min(query))
        else:
            result.append(-1)
    return result
    