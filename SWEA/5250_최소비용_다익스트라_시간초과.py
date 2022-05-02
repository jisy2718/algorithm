# 배열의 한 방향으로의 값이 같으면, while문으로 계속 이동해서, 최소 거리로 update 가능! -> 그럼 제한시간 초과 없어지지 않을까?

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

    # 현재위치 표기 및 cost, used 초기화
    cr, cc = sr, sc
    INF = 100*1000
    cost = [[INF]*N for _ in range(N)]
    used = {(cr,cc)}
    cost[cr][cc] = 0
    while cr != er or cc!= ec:
        # 갈 수 있는 곳들 중 이동비용 계산
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 새로운 노드에서, 다른 곳으로 이동할 때, 기존
            if 0<=nr<N and 0<=nc<N and (nr,nc) not in used:
                # (sr,sc) -> (cr,cc) -> (nr,nc) < (sr,sc) -> (nr,nc) 경우에 업데이트
                if cost[cr][cc] + 1 + max(0,arr[nr][nc]-arr[cr][cc]) < cost[nr][nc]:
                    cost[nr][nc] = cost[cr][cc] + 1 + max(0,arr[nr][nc]-arr[cr][cc])

        # 갈 수 있는 곳들의 minimum 이동비용위치 계산
        min_r = -1
        min_c = -1
        min_val = INF
        for r in range(N):
            for c in range(N):
                if (r,c) not in used and cost[r][c] < min_val:
                    min_val = cost[r][c]
                    min_r = r
                    min_c = c


        # 최소 비용인 곳으로 이동
        used.add((min_r,min_c))
        cr = min_r
        cc = min_c


    print(f"#{tc} {cost[er][ec]}")






