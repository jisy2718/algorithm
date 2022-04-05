# 이동 / 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

T = int(input())
for tc in range(1,T+1):
    # input
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 출발 도착
    sr, sc = 0, 0
    er, ec = N-1, N-1


    # 현재 위치에서, 이동비용 list로 생성
    # 최소 비용으로 이동 후 목적지 인지 확인

    # 최소 비용으로 이동 후, 이동 비용 list update
    # 목적지에 도달할 때까지 반복

    # visited, used , queue 초기화
    INF = 100*1000
    visited = [[INF]*N for _ in range(N)]
    visited[sr][sc] = 0
    queue = [[sr,sc]]
    while queue:
        cr, cc = queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 이동 경로가 유효하고, 기존보다 비요이 적은 경우
            if 0 <= nr < N and 0 <= nc < N and visited[cr][cc] + 1 + max(arr[nr][nc] - arr[cr][cc],0) < visited[nr][nc]:
                #
                # for row in visited:
                #     print(row)
                # print("-------------------------")

                visited[nr][nc] = visited[cr][cc] + 1 + max(arr[nr][nc] - arr[cr][cc],0)

                queue.append([nr,nc])
    print(f"#{tc} {visited[er][ec]}")






