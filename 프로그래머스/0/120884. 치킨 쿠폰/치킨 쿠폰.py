def solution(chicken):
    service = 0 
    coupon = chicken # 1닭 1쿠폰
    
    while coupon >= 10:
        free = coupon // 10 # 10장 1닭
        service += free
        coupon = free + (coupon % 10)
        
    return service
    
    