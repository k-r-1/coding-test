def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(n) + 1 for n in emergency]