import re

def solution(my_string, alp):
    answer = ''
    answer += re.sub(alp, alp.upper(), my_string)
    return answer