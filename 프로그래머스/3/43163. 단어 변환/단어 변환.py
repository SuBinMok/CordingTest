from collections import deque
def solution(begin, target, words):
    answer = 9999
    n = len(begin)
    stack = deque([[begin, 0]])
    visited = [False]*len(words)
    
    while stack:
        b, t = stack.pop()
        for i in range(len(words)):
            cnt = 0
            if visited[i] == False:
                for j in range(n):# 단어 중 같은 알파벳이 몇 개 인지 확인
                    if words[i][j] == b[j]:
                        cnt +=1
                if cnt == (n-1):
                    visited[i] = True
                    stack.append([words[i], t+1])
        if b == target and answer > t:
            answer = t
    if answer == 9999:
        return 0
    return answer