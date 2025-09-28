def solution(arr, queries):
    for s, e, k in queries:
        query = [i for i in range(s, e+1) if i % k == 0]
        for i in query:
            arr[i] += 1
    return arr