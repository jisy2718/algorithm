from collections import deque

# 이동 규칙 1시부터 시계방향
dr = [-2, -1, 1, 2, 2, 1, -2, -1]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
T = int(input())

for _ in range(T):
    I = int(input())  # 체스판 크기
    sr, sc = map(int, input().split())  # 시작점
    er, ec = map(int, input().split())  # 끝점
    visited = [[False] * I for _ in range(I)]

    queue = deque()
    queue.append([sr, sc, 0])
    cur_min = 100000
    while queue:
        cr, cc, cdistance = queue.popleft()
        if cr == er and cc == ec and cur_min>cdistance:
            cur_min = cdistance

        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == False:
                queue.append([nr, nc, cdistance + 1])
                visited[nr][nc] = True
    print(cur_min)
