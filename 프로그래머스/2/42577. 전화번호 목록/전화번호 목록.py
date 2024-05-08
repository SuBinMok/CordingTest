def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i, j in zip(phone_book, phone_book[1:]): #zip을 사용하면 이중 for문을 사용하지 않아도 된다.
        if j.startswith(i): #starts with: j 문자열이 (i)부터 시작하는지 확인하는 변수
            return False
        
    return answer