def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
            if len(stk) == 0:
                stk.append(arr[i])
                i += 1
            elif stk is not None and (stk[-1] < arr[i]):
                stk.append(arr[i])
                i += 1
            elif stk is not None and (stk[-1] >= arr[i]):
                stk.remove(stk[-1])
    return stk
