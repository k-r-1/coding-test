import re

def solution(myStr):
    parts = re.split("[abc]", myStr)
    parts = [ch for ch in parts if ch != '']
    return parts if parts else ["EMPTY"]