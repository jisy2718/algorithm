

#-----------------------------------sol1 : 모든 경우의 수 풀이--------------------------
N, M = map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(N) ]
result = 0

# 회전 & 대칭 가능
# N,M >=4
# 1 . ---- / L / ㅗ 형태 : 3개 연달아 더하고, 주변의 것 1개 씩 더해주면 됨
# 1-1. --- 더하는 경우
for r in range(N):
    for c in range(M-2):
        cur_sum = arr[r][c] + arr[r][c+1] + arr[r][c+2]
        for dr in [-1,1]:
            for dc in [0,1,2]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N:
                    new_sum = cur_sum + arr[nr][nc]
                    if new_sum > result:
                        result = new_sum
        # ---- 경우
        if 0 < c+3 < M:
            new_sum = cur_sum + arr[r][c+3]
            if new_sum > result:
                result = new_sum




# 1-2. ㅣ 로 3개 더하는 경우
for r in range(N-2):
    for c in range(M):
        cur_sum = arr[r][c] + arr[r+1][c] + arr[r+2][c]
        for dc in [-1,1]:
            for dr in [0,1,2]:
                nr = r + dr
                nc = c + dc
                if 0 <= nc < M:
                    new_sum = cur_sum + arr[nr][nc]
                    if new_sum > result:
                        result = new_sum
        # ---- 경우
        if 0 < r+3 < N:
            new_sum = cur_sum + arr[r+3][c]
            if new_sum > result:
                result = new_sum

# 2. 네모 / z 타입
# 2-1. -- 다 더해서 아래부분에 -- 더 더해주면 됨
for r in range(N):
    for c in range(M-1):
        cur_sum = arr[r][c] + arr[r][c+1]
        for dr in [1]:
            for dc in [-1,0,1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if dc == -1:
                        new_sum = cur_sum + arr[nr][nc] + arr[nr][nc+1]
                    elif dc == 0:
                        new_sum = cur_sum + arr[nr][nc] + arr[nr][nc+1]
                    elif dc == 1:
                        if nc + 1 < M:
                            new_sum = cur_sum + arr[nr][nc] + arr[nr][nc + 1]

                    if new_sum > result:
                        result = new_sum


# 2-2. l 로 2개 더해서 오른쪽 부분에 l 더 더해주면 됨
for r in range(N-1):
    for c in range(M):
        cur_sum = arr[r][c] + arr[r+1][c]
        for dc in [1]:
            for dr in [-1, 0, 1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if dr == -1:
                        new_sum = cur_sum + arr[nr][nc] + arr[nr+1][nc]
                    elif dr == 0:
                        new_sum = cur_sum + arr[nr][nc] + arr[nr+1][nc]
                    elif dr == 1:
                        if nr + 1 < N:
                            new_sum = cur_sum + arr[nr][nc] + arr[nr+1][nc]

                    if new_sum > result:
                        result = new_sum
print(result)

#--------------------------------------------------------------

#
# #-----------------------------------------------------sol2 : dfs / ㅗ모양 추가처리해줘야함------------------
#
# N, M = map(int,input().split())
#
# arr = [ list(map(int,input().split())) for _ in range(N) ]
# result = 0
# # 그냥 4칸 붙어있는 것 중에 최대 값 찾으면 됨
# # 이동 / 상우하좌
# dr = [1,0,1,0]
# dc = [0,1,0,-1]
# def dfs(cr,cc, c_box, c_sum):
#     global result
#     if c_box == 4:
#         if c_sum > result:
#             result = c_sum
#             # print(f'result = {result} , cr,cc = {cr},{cc}')
#
#     else:
#         for i in range(len(dr)):
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]==0:
#                 visited[nr][nc] = 1
#                 dfs(nr,nc,c_box+1, c_sum+arr[nr][nc])
#
#
# for r in range(N):
#     for c in range(M):
#         visited = [[0]*M for _ in range(N)]
#         visited[r][c] = 1
#         dfs(r,c,1,arr[r][c])
# print(result)