#-----------------------------------재귀 아닌 버전-----------------------------------------
# def nqueen(cur_r):
#     global result
#     r = cur_r
#     if r == N:
#         result += 1
#
#     else:
#         for c in range(N):
#             cr, cc = r, c
#             if promising(cr, cc): # cr, cc가 유망한지 탐색
#                 col[cc] = 1
#                 right_diag[N - 1 + (cr - cc)] = 1
#                 left_diag[cr + cc] = 1
#                 nqueen(cr + 1)
#                 col[cc] = 0
#                 right_diag[N - 1 + (cr - cc)] = 0
#                 left_diag[cr + cc] = 0
#     return
#
#
# def promising(cr, cc):
#     if col[cc] == 0 and right_diag[N - 1 + (cr - cc)] == 0 and left_diag[cr + cc] == 0:
#         return True
#     else:
#         return False
#
# for i in range(1,16):
#     N = i
#
#
#     arr = [[0]*N for _ in range(N)]
#     col = [0]*N
#     right_diag = [0]*(2*N-1) # \ 방향 대각선 r-c = -(N-1), -(N-2) , ... 0, 1, ... N-2, N-1    \\\\\ + N -1 = -> 0, 1, 2 ,, 2N-1
#     left_diag = [0]*(2*N-1) # / 방향 대각선 r+c = 0, 1, 2, 3, ... , 2N-2 //
#     result = 0
#     nqueen(0)
#     print(f"N : {N}, result : {result}")
#--------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------dfs of tree 풀이 -----------------------------------

def check(sr, sc):
    # column
    for r in range(sr-1,-1,-1):
        # column
        if visited[r][sc] == 1:
            return False
        # 좌측 위 대각선
        if 0 <= sc - (sr-r) and visited[r][sc-(sr-r)] == 1:  # column이 1,2,3,4,... 씩 index 줄어야
            return False
        # 우측 위 대각선
        if sc + (sr-r) < N and visited[r][sc+(sr-r)] == 1:   # column이 1,2,3,4,... 씩 index 늘어야
            return False
    return True

def dfs(r):
    global cnt
    if r == N:
        cnt += 1
        return
    else:
        for c in range(N):
            if check(r,c):
                visited[r][c] = 1
                dfs(r+1)
                visited[r][c] = 0


N = int(input())
visited = [[0]*N for _ in range(N)]
cnt = 0
dfs(0)
print(cnt)