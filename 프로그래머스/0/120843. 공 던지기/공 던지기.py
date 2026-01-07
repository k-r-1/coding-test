def solution(numbers, k):
    idx = 0
    n_len = len(numbers)
    for _ in range(k-1):
        idx = (idx + 2) % n_len
        
    return numbers[idx]