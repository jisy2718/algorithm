M, N, K = map(int,input().split())

arr = [[0]*N for _ in range(M)]

for _ in range(K):
    sx, sy, ex, ey = map(int,input().split())
    for x in range(sx,ex):
        for y in range(sy,ey):
            arr[y][x] = 1

region = 0
total_count = []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            q = []
            q.append([r,c])
            arr[r][c ] = 1
            count = 1
            while q:
                cr, cc = q.pop(0)

                for move in [[0,1],[0,-1],[-1,0],[1,0]]:
                    nr = cr + move[0]
                    nc = cc + move[1]

                    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
                        q.append([nr,nc])
                        arr[nr][nc] = 1
                        count += 1

            # 영역 개수 + 1
            region += 1
            # 영역 크기 추가
            total_count.append(count)

total_count.sort()
print(region)
print(*total_count)



