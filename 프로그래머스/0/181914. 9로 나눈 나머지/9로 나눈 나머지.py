def solution(number):
    digit_num = sum(map(int, number))
    return digit_num % 9
    