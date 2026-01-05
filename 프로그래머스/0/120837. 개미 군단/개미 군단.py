def solution(hp):
    # 장군개미 5 공격력
    # 병정개미 3 공격력
    # 일개미 1 공격력
    
    count = 0
    
    count += hp // 5
    hp = hp % 5
    
    count += hp // 3
    hp = hp % 3
    
    count += hp // 1
    hp = hp % 1
    
    return count
    