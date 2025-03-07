def solution(num_list):
    s = sum(num_list)
    p = 1
    for num in num_list:
        p *= num
    return 1 if p < s**2 else 0