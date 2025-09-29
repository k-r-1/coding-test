def solution(n):
    # 현재 값이 x면 짝수일 때 2로 나누고
    # 홀수일 때 3 * x + 1로 바꾸는 계속 반복
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result
    