def solution(num_list):
    odd = ''
    even = ''
    
    for n in num_list:
        if n % 2 == 1: 
            odd += str(n)
        else:
            even += str(n)
    result = int(odd) + int(even)
    return result