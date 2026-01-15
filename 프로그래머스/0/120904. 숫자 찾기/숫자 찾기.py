def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    
    return str_num.index(str_k) + 1 if str_k in str_num else -1
    