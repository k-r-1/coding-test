from collections import Counter 

def solution(array):
    counter = Counter(array)
    # 가장 많이 나온 횟수 
    max_count = max(counter.values())
    # 최빈값
    result = [k for k, v in counter.items() if v == max_count]
    return result[0] if len(result) == 1 else -1