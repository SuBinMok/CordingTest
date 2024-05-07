def solution(id_pw, db):
    answer = ''
    for id, pw in db:
        if id_pw[1] == pw and id_pw[0] == id:
            answer = 'login'
            break
        if id_pw[1] != pw and id_pw[0]  == id:
            answer = 'wrong pw'
            continue
        if id_pw[0] != id and id_pw[1] != pw:
            if answer != 'wrong pw':
                answer = 'fail'
            continue
        
        
        
    return answer