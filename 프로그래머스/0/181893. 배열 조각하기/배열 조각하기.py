def solution(arr, query):
    answer = []
    for i, v in enumerate(query):
        if i % 2 == 0:
            arr = arr[:query[i] + 1]
        else:
            arr= arr[query[i]:]
    return arr

