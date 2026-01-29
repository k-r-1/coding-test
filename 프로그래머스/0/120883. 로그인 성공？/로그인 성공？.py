def solution(id_pw, db):
    
    user_id, user_pw = id_pw
    
    for id, pw in db:
        if id == user_id:
            if pw == user_pw:
                return "login"
            else:
                return "wrong pw"
    return "fail"
        