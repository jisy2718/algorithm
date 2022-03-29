import sys
sys.stdin = open('4615_input.txt')

from pprint import pprint

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [[0]*(N+1)] + [[0]*(N+1) for _ in range(N)]
    arr[N//2][N//2] = 2 # 흑1, 백 -1
    arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = 1
    arr[N//2][N//2+1] = 1

    def search(r,c,cur_color):
        get = [[r,c]] # result
        if cur_color == 2:
            target_color = 1
        else: # cur_color == 1
            target_color = 2
        # 탐색방향 : 12 시부터 시계방향
        dr = [-1,-1,0,1,1, 1, 0,-1]
        dc = [0,  1,1,1,0,-1,-1,-1]
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            tmp = []

            while 1 <= nr < N+1 and 1 <= nc <N+1  and arr[nr][nc] == target_color:
                cr = nr
                cc = nc
                # print(f"{cr},{cc} 추가 {tmp}")
                tmp.append([cr,cc])
                nr = cr + dr[d]
                nc = cc + dc[d]
                # print(nr,nc)

            # 유효칸에 안착 가능한 경우만 tmp를 get에 넣기
            if 1 <= nr < N+1 and 1 <= nc <N+1  and arr[nr][nc] == cur_color:
                get.extend(tmp)

        return get


    for _ in range(M):
        c,r,cur_color = map(int,input().split()) # column, row 순으로 들어옴
        result = search(r,c,cur_color)
        for loc in result:
            nr, nc = loc
            arr[nr][nc] = cur_color

    black = 0
    white = 0
    for r in range(1,N+1):
        for c in range(1,N+1):
            if arr[r][c] == 1:
                black +=1
            elif arr[r][c] == 2:
                white += 1

    print(f"#{tc} {black} {white}")



