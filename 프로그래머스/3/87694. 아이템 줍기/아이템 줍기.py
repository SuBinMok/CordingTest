from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    queue = deque()
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    # line 구하기
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2: #사각형 내부를 0으로 채우기
                    graph[i][j] = 0
                elif graph[i][j] != 0: # 사각형 내부가 아니면...
                    graph[i][j] = 1
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    queue.append([cx, cy])
    while queue:
        x, y = queue.popleft()
        if x == ix and y == iy:
            answer = visited[x][y] // 2
            return answer
        else:
            for k in range(len(d)):
                nx, ny = x+d[k][0], y+d[k][1]
                if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] += visited[x][y]
                