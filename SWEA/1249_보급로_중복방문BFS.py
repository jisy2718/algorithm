import sys
sys.stdin = open("1249_input.txt")

# 이동 / 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited =[ [10**8]*N  for _ in range(N)]

    sr, sc = 0, 0
    er, ec = N-1, N-1

    queue = [[sr,sc]]
    visited[sr][sc] = arr[sr][sc]
    while queue:
        cr, cc = queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] > visited[cr][cc] + arr[nr][nc] :
                    queue.append([nr,nc])
                    visited[nr][nc] = visited[cr][cc] + arr[nr][nc]


    print(f"#{tc} {visited[N-1][N-1]}")



