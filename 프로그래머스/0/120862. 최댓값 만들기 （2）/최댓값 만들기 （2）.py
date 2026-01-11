def solution(numbers):
    numbers.sort()
    left = numbers[0] * numbers[1]
    right = numbers[-1] * numbers[-2]
    
    return max(left, right)