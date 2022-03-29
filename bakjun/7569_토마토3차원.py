import sys

M, N, H = map(int, input().split())  # 가로, 세로, 높이
# 1층 ~ H 층순으로 input 입력됨

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# 1 : 익은 토마토, 0 : 익지않은 토마토, -1 : 빈 칸


# 이동 / 상우하좌,수직위 수직아래
dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

# queue
queue = []
target = 0  # 0의 개수(익지않은 토마토 개수)
# 가장 밖에 큰 것에서부터 loop
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] >= 1:
                queue.append([h, r, c])
            elif arr[h][r][c] == 0:
                target += 1

total_day = 1
while queue:
    ch, cr, cc = queue.pop(0)

    for i in range(6):
        nh = ch + dh[i]
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
            arr[nh][nr][nc] = arr[ch][cr][cc] + 1
            target -= 1  # 익지 않은 토마토 개수
            queue.append([nh, nr, nc])

            if total_day < arr[nh][nr][nc]:
                total_day = arr[nh][nr][nc]

# 결과
if target != 0:
    print(-1)
else:
    print(total_day - 1)