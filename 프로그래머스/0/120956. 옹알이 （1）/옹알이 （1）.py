def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        temp = word
        
        for c in can:
            temp = temp.replace(c, " ")
            
        if temp.replace(" ", "") == "":
            count += 1
            
    return count         
            
            