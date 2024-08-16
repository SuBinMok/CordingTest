from collections import deque
"""
DFS
"""
def solution(tickets):
    answer = ['ICN']
    for t in tickets:
        t.append(0)
    num = len(tickets)+1
    tickets.sort(key = lambda x: x[1])
    def dfs(dep):
        for ticket in tickets:
            if ticket[0] == dep and ticket[2] == 0:
                answer.append(ticket[1])
                ticket[2] = 1
                if len(answer) == num or dfs(ticket[1]):
                    return answer
                ticket[2] = 0
                answer.pop()
    dfs(answer[0])
    return answer