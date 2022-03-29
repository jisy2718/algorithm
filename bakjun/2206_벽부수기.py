from collections import deque
from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# print(arr)
# 이동방향 / 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# BFS 탐색
queue = deque()
queue.append([0, 0, 0, 1])  # x,y 좌표 & 벽을 부순 횟수 & 이동거리
visited[0][0] = True
flag = False
while queue:
    cr, cc, b, distance = queue.popleft()
    # print(cr,cc)

    # 목적지 다다르면, print
    if cr == N - 1 and cc == M - 1:
        print(distance)
        flag = True
        break

    # 탐색
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        # print(f"nr nc {nr}{nc}")
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False:
            if arr[nr][nc] == 0:
                queue.append([nr, nc, b, distance + 1])
                visited[nr][nc] = True


            elif arr[nr][nc] == 1 and b == 0:
                queue.append([nr, nc, 1, distance + 1])
                visited[nr][nc] = True

if flag == False:
    print(-1)
