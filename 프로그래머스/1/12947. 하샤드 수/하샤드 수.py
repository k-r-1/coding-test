def solution(x):
    digit_list = [int(digit) for digit in str(x)]
    
    digit_sum = sum(digit_list)
    
    return x % digit_sum == 0