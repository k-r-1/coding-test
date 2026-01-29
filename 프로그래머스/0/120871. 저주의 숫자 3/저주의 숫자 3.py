def solution(n):
    count = 0
    num = 0
    
    while True:
        num += 1
        
        if (num % 3 != 0) and ('3' not in str(num)):
            count += 1
            
            if count == n:
                return num
     