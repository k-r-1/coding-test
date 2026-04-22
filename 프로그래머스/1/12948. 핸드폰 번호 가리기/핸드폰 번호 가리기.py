def solution(phone_number):
    length = len(phone_number)
    mask = length - 4
    answer = "*" * mask + phone_number[-4:]
    return answer