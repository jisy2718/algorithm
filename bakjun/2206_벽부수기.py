
# from collections import deque
#
# N, M = map(int, input().split())
#
# arr = [list(map(int, input())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# # print(arr)
# # 이동방향 / 상우하좌
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# # BFS 탐색
# queue = deque()
# queue.append([0, 0, 0, 1])  # x,y 좌표 & 벽을 부순 횟수 & 이동거리
# visited[0][0] = True
# flag = False
# while queue:
#     cr, cc, b, distance = queue.popleft()
#     # print(cr,cc)
#
#     # 목적지 다다르면, print
#     if cr == N - 1 and cc == M - 1:
#         print(distance)
#         flag = True
#         break
#
#     # 탐색
#     for i in range(4):
#         nr = cr + dr[i]
#         nc = cc + dc[i]
#         # print(f"nr nc {nr}{nc}")
#         if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False:
#             if arr[nr][nc] == 0:
#                 queue.append([nr, nc, b, distance + 1])
#                 visited[nr][nc] = True
#
#
#             elif arr[nr][nc] == 1 and b == 0:
#                 queue.append([nr, nc, 1, distance + 1])
#                 visited[nr][nc] = True
#
# if flag == False:
#     print(-1)

#------------------------bfs 함수 with 3차원visited--------------------------
from collections import deque
def bfs(sr,sc,br,distance): # 행, 열, 이동거리, 벽부순횟수

    q = deque([])
    q.append([sr,sc,br,distance])
    visited[sr][sc][br] = 1
    while q:
        cr, cc, cbr, cdistance  = q.popleft()

        if cr == N-1 and cc == M-1:
            return cdistance

        # 이동
        for d in ([-1,0],[1,0],[0,1],[0,-1]):
            nr = cr + d[0]
            nc = cc + d[1]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][cbr]==0:
                if arr[nr][nc] == 1 and cbr == 0:
                    q.append([nr,nc,cbr+1,cdistance+1])
                    visited[nr][nc][cbr+1] = 1
                elif arr[nr][nc] == 0:
                    q.append([nr,nc,cbr,cdistance+1])
                    visited[nr][nc][cbr] = 1



    return -1
N, M = map(int,input().strip().split())


arr = [list(map(int,input())) for _ in range(N)]


visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

sr = sc = sbr = 0
distance = 1

result = bfs(sr,sc,sbr,distance)

print(result)






