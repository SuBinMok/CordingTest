def solution(s, skip, index):
    answer = ''
    dic = [chr(i) for i in range(ord("a"), ord("z")+1) if chr(i) not in skip]
    n = 0
        
    for string in s:
        num = dic.index(string) + index
        num = num % (len(dic))
        answer += dic[num]
            
    return answer