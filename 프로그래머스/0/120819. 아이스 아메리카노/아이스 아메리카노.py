def solution(money):
    cup = 0
    
    while money >= 5500:
        cup += 1
        money = money - 5500
    
    return [cup, money]