def solution(num, total):
    avg = total // num
    start = avg - ((num - 1) // 2)
    return list(range(start, start + num))
    