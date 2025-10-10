from collections import Counter

def solution(a, b, c, d):
    nums = [a, b, c, d]
    unique = set(nums) 
    cnt = Counter(nums) 
    score = 0
    
    
    if len(unique) == 1: # 4개 같을 때
        p = nums[0]
        score = 1111 * p
    elif len(unique) == 2: # 3개 같고 1개 다를 때 / 2개 씩 다른 값일 때
        if 3 in cnt.values():
            p = [k for k, v in cnt.items() if v == 3][0]
            q = [k for k, v in cnt.items() if v == 1][0]
            score = (10 * p + q) ** 2
        elif 2 in cnt.values():
            p, q = cnt.keys()
            score = (p + q) * abs(p - q)
    elif len(unique) == 3: # 한 쌍만 같을 때 (2 / 1 / 1)
        p = [k for k, v in cnt.items() if v == 2][0]
        # q != r
        others = [k for k, v in cnt.items() if v == 1]
        q, r = others 
        score = q * r
        
    else: # 모두 다를 때
        score = min(cnt)
    
    return score

    