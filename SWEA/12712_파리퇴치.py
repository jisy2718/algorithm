T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상우하좌
    dr1 = [-1, 0, 1, 0]
    dc1 = [0, 1, 0, -1]

    # 1시,5시,7시,11시
    dr2 = [-1, 1, 1, -1]
    dc2 = [1, 1, -1, -1]

    dr = [dr1, dr2]
    dc = [dc1, dc2]

    max_cnt = 0
    # 점검
    for r in range(N):
        for c in range(N):
            for i in range(2):  # +, * 방향
                cur_cnt = arr[r][c]
                for d in range(4):
                    for m in range(1, M ):
                        nr = r + dr[i][d] * m
                        nc = c + dc[i][d] * m
                        if 0 <= nr < N and 0 <= nc < N:
                            cur_cnt += arr[nr][nc]
                if max_cnt < cur_cnt:
                    max_cnt = cur_cnt
    print(f"#{tc} {max_cnt}")

