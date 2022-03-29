# 1. input
N, M = map(int, input().split())
from collections import deque
import sys

arr = [[0] * (M + 1)] + [[0] + list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * (M + 1) for _ in range(N + 1)]
# 2. 시작점
sr, sc = 1, 1

# 3. 이동규칙 (상우하좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dq = deque([])
distance = 1
dq.append([sr, sc, distance])  # 첫 칸도 거리에 포함됨

while dq:
    cr, cc, distance = dq.popleft()
    visited[cr][cc] = True
    # 만약 목적지라면 출력하고 그만!
    if cr == N and cc == M:
        print(distance)
        break

    # 현재 것 기준으로 탐색
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        # 조건 확인
        if 1 <= nr <= N and 1 <= nc <= M and arr[nr][nc] == 1 and visited[nr][nc] == False:
            # dq 추가 (모두 한 번에)
            dq.append([nr, nc, distance + 1])
