def solution(n):
    answer = 0
    if n % 2 == 1: # 홀수라면
        for i in range(1, n+1, 2): # n 이하의 홀수인 모든 양의 정수의 합
            answer += i
        return answer
    else: # 짝수라면
        for i in range(2, n+1, 2): # n 이하의 짝수인 모든 양의 정수의 제곱의 합
            answer += i ** 2
        return answer
        