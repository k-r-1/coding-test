def solution(order):
    total = 0
    for s in order:
        if "cafelatte" in s:
            total += 5000
        else:
            total += 4500
    return total 