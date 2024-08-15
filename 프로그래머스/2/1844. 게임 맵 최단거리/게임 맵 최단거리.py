from collections import deque
def solution(maps):
    answer = 99999
    queue = deque()
    queue.append([1, 0, 0])
    visited = maps.copy()
    n = len(maps)
    m = len(maps[0])
    # if (maps[n-2][m-1]==0) and (maps[n-1][m-2]==0):
    #     return -1
    cx, cy = 0, 0
    while queue:
        move, x, y = queue.popleft()
        cx, cy = x, y
        if x == n-1 and y == m-1 and answer > move:
            answer = move
        if 0 <= x - 1 < n and 0 <= y < m and maps[x-1][y] == 1 and visited[x-1][y] == 1:
            #상
            queue.append([move+1, x-1, y])
            visited[x-1][y] = move
        if 0 <= x + 1 < n and 0 <= y < m and maps[x+1][y] == 1 and visited[x+1][y] == 1:
            #하
            queue.append([move+1, x+1, y])
            visited[x+1][y] = move
        if 0 <= x < n and 0 <= y - 1 < m and maps[x][y-1] == 1 and visited[x][y-1] == 1:
            #좌
            queue.append([move+1, x, y-1])
            visited[x][y-1] = move
        if 0 <= x < n and 0 <= y + 1 < m and maps[x][y+1] == 1 and visited[x][y+1] == 1:
            #우
            queue.append([move+1, x, y+1])
            visited[x][y+1] = move
    if visited[n-1][m-1] != 1:
        return answer
    else: 
        return -1
    #BFS를 사용해야한다!
    #따라서 queue를 사용하여 시작점 주변에서 갈 수 있는 인접한 모든 노드를 넣는다. (상하좌우)
    #도착했을 때 count 수가 answer보다 작으면 update를 해준다.
    #이진트리 했을 때처럼 상하좌우에서 1인 경우, 모두 append를 한 뒤에 값을 구함..? => 속도가 느림.
    #visited를 선언해서 간 곳은 false, 안간곳은 true, true인 경우만 움직이게 함.
    #queue에 넣는 값은 움직인 거리와 위치 정보를 넣기.[move+1, [x, y]]
    #탐색을 했을 때 visited => true이면 queue.append([move+1, x, y])
    
    
    return answer