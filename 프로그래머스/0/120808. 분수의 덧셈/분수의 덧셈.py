from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2 
    
    # 최대공약수로 약분
    g = gcd(numer, denom)
    numer = numer // g
    denom = denom // g
    
    return [numer, denom]
    