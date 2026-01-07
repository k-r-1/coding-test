def solution(rsp):
    table = {"2":"0", "0":"5", "5":"2"}
    return "".join(table[key] for key in rsp)