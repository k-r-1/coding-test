def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        num_int = int(num_str[s:s+l])
        if num_int > k:
            answer.append(num_int)
        
    return answer