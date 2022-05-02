# 자신의 크기, 물고기 먹은 갯수 필요
# bfs 접근에 좌표 필요
# bfs는 위쪽, 좌측, 아래, 우측 순으로 진행
#
# dr = [-1, 0, 0, 1] # 상 좌 우 하
# dc = [0, -1, 1, 0]
#
#
#
# # 물고기를 지나갈 수 있으면 지나가기
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N) ]
# count = [0]*7  # 물고기 개수
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 9:
#             sr = r
#             sc = c
#         elif arr[r][c] in [1,2,3,4,5,6]:
#             count[arr[r][c]] += 1
#
#
#
# from collections import deque
#
#
# def bfs(cr, cc, c_size, ce_count, ct):
#     q = deque()
#     q.append([cr,cc,c_size,ce_count, ct])
#
#     while q:
#         # print(q[0][0:2])
#         cr, cc, c_size, ce_count, ct = q.popleft()
#
#
#
#         # 더이상 먹을 것 없음
#         if sum(count[:c_size]) == 0:
#             return ct
#
#         # 탐색
#         for i in range(4):
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             if 0 <= nr < N and 0 <= nc < N:
#                 # 크기 같으면 통과
#                 if arr[nr][nc] == c_size or arr[nr][nc]==0:
#                     q.append([nr, nc, c_size, ce_count, ct + 1])
#
#                 # 먹는 경우
#                 elif 1 <= arr[nr][nc] < c_size:
#                     ce_count += 1
#                     count[arr[nr][nc]] -= 1
#                     arr[nr][nc] = 0
#
#                     if ce_count == c_size:
#                         c_size += 1
#                         ce_count = 0
#
#
#                     return bfs(nr,nc,c_size, ce_count, ct+1)
#
# sr = sr
# sc = sc
# s_size = 2   # 현재크기
# e_count = 0  # 먹은 물고기 개수
# t = 0        # 걸린 시간
#
#
#
# result = bfs(sr,sc,s_size,e_count, t)
# print(result)
#--------------------------------------------------------------------------------------------------


# 왼쪽 상단부터 루프돌면서, 거리재는 방법

#
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N) ]
# # for row in arr:
# #     print(row)
# # print()
# count = [0]*7  # 물고기 개수
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 9:
#             sr = r
#             sc = c
#         elif arr[r][c] in [1,2,3,4,5,6]:
#             count[arr[r][c]] += 1
# #
# #
# # def dist(cr,cc,cur_size, cur_move, tr,tc):
# #     global cur_dist
# #     if cur_dist < cur_move:
# #         return
# #
# #     if cur_move > N*N:
# #         return
# #
# #     if cr == tr and cc == tc:
# #         return cur_move
# #
# #     else:
# #         if 0 <= cr < N and 0<= cc - 1 < N and arr[cr][cc-1] <= cur_size:
# #             dist(cr,cc-1,cur_size,cur_move+1, tr,tc)
# #
# #         if 0 <= cr < N and 0 <= cc + 1 < N and arr[cr][cc + 1] <= cur_size:
# #             dist(cr, cc + 1, cur_size, cur_move + 1, tr, tc)
# #
# #         if 0 <= cr - 1 < N and 0 <= cc < N and arr[cr-1][cc] <= cur_size:
# #             dist(cr-1, cc, cur_size, cur_move + 1, tr, tc)
# #
# #         if 0 <= cr + 1 < N and 0 <= cc < N and arr[cr+1][cc] <= cur_size:
# #             dist(cr+1, cc , cur_size, cur_move + 1, tr, tc)
#
#
# def dist(cr,cc,cur_size, cur_move, tr,tc):
#
#     visited = [[0]*N for _ in range(N)]
#
#
#
#     c_move = 0
#     q = [[cr, cc, c_move]]
#     visited[cr][cc] = 1
#
#     while q:
#         cr, cc, c_move = q.pop(0)
#
#
#         if c_move > N*N:
#             return
#
#         if cr == tr and cc == tc:
#             return c_move
#
#         if 0 <= cr < N and 0<= cc - 1 < N and arr[cr][cc-1] <= cur_size and visited[cr][cc-1]==0:
#             q.append([cr,cc-1,c_move+1])
#             visited[cr][cc-1] = 1
#
#         if 0 <= cr < N and 0 <= cc + 1 < N and arr[cr][cc + 1] <= cur_size and visited[cr][cc+1]==0:
#             q.append([cr,cc+1,c_move+1])
#             visited[cr][cc+1] = 1
#
#         if 0 <= cr - 1 < N and 0 <= cc < N and arr[cr-1][cc] <= cur_size and visited[cr-1][cc]==0:
#             q.append([cr-1,cc,c_move+1])
#             visited[cr-1][cc] = 1
#
#         if 0 <= cr + 1 < N and 0 <= cc < N and arr[cr+1][cc] <= cur_size and visited[cr+1][cc]==0:
#             q.append([cr+1,cc,c_move+1])
#             visited[cr+1][cc] = 1
#
#
# def find_fish(cr,cc,cur_size,cur_eat):
#     global flag
#     # 물고기 찾기
#     # 좌측 상단부터 시작!
#     min_dist = 0xffffff
#     min_r = -1
#     min_c = -1
#     for r in range(N):
#         for c in range(N):
#             if 1<= arr[r][c] < cur_size:
#                cur_dist = dist(cr,cc,cur_size,0,r,c)
#                if cur_dist==None:
#                    flag = False
#                    return cr, cc, cur_size, cur_eat, 0
#
#
#
#                if min_dist > cur_dist:
#                    min_dist = cur_dist
#                    min_r = r
#                    min_c = c
#
#     if min_dist == 0xffffff:
#         flag = False
#         return cr,cc,cur_size,cur_eat, 0
#
#
#     # 이동해서 먹기
#     count[arr[min_r][min_c]] -= 1
#     arr[min_r][min_c] = 0
#     now_moved = min_dist
#     cur_eat += 1
#
#     # cur_size 및 cur_eat 변경사항 반영
#     if cur_eat == cur_size:
#         cur_size += 1
#         cur_eat = 0
#
#     return min_r, min_c, cur_size, cur_eat, now_moved
#
#
# cr = sr
# cc = sc
# cur_size = 2
# cur_eat = 0
# result = 0
# flag = True
# arr[cr][cc] = 0
# while sum(count[:cur_size]) != 0 and flag==True:
#     cr, cc, cur_size, cur_eat, now_moved = find_fish(cr,cc,cur_size,cur_eat)
#
#     # for row in arr:
#         # print(row)
#     # print(cr, cc, cur_size, cur_eat, now_moved)
#     result += now_moved
#
# print(result)
#




#----------------------------------------------------------------------------------------------------------------

#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N) ]
#
# count = [0]*7  # 물고기 개수
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 9:
#             sr = r
#             sc = c
#         elif arr[r][c] in [1,2,3,4,5,6]:
#             count[arr[r][c]] += 1
#
#
#
# def bfs(cr,cc,c_size,c_eat,c_move):
#     visited = [[0]*N for _ in range(N)]
#     q = [[cr, cc, c_size, c_eat, c_move]]
#     visited[cr][cc] = 1
#     result = []
#     while q:
#         cr, cc, c_size, c_eat, c_move = q.pop(0)
#         if c_size >=1 and not result:
#             result.append([c_size,cr,cc])
#
#         elif c_size >= 1 and result:
#             if result[0] == c_size:
#                 result.append([c_size,cr,cc])
#             else:
#                 return
#         result.sort()
#
#
#
#         if 0 <= cr < N and 0<= cc - 1 < N and arr[cr][cc-1] <= c_size and visited[cr][cc-1]==0:
#             q.append([cr,cc-1,c_move+1])
#             visited[cr][cc-1] = 1
#
#         if 0 <= cr < N and 0 <= cc + 1 < N and arr[cr][cc + 1] <= c_size and visited[cr][cc+1]==0:
#             q.append([cr,cc+1,c_move+1])
#             visited[cr][cc+1] = 1
#
#         if 0 <= cr - 1 < N and 0 <= cc < N and arr[cr-1][cc] <= c_size and visited[cr-1][cc]==0:
#             q.append([cr-1,cc,c_move+1])
#             visited[cr-1][cc] = 1
#
#         if 0 <= cr + 1 < N and 0 <= cc < N and arr[cr+1][cc] <= c_size and visited[cr+1][cc]==0:
#             q.append([cr+1,cc,c_move+1])
#             visited[cr+1][cc] = 1
#
#
#
# #
# #
# #
# #
# #     c_move = 0
# #     q = [[cr, cc, c_move]]
# #     visited[cr][cc] = 1
# #
# #     while q:
# #         cr, cc, c_move = q.pop(0)
# #
# #
# #         if c_move > N*N:
# #             return
# #
# #         if cr == tr and cc == tc:
# #             return c_move
# #
# #         if 0 <= cr < N and 0<= cc - 1 < N and arr[cr][cc-1] <= cur_size and visited[cr][cc-1]==0:
# #             q.append([cr,cc-1,c_move+1])
# #             visited[cr][cc-1] = 1
# #
# #         if 0 <= cr < N and 0 <= cc + 1 < N and arr[cr][cc + 1] <= cur_size and visited[cr][cc+1]==0:
# #             q.append([cr,cc+1,c_move+1])
# #             visited[cr][cc+1] = 1
# #
# #         if 0 <= cr - 1 < N and 0 <= cc < N and arr[cr-1][cc] <= cur_size and visited[cr-1][cc]==0:
# #             q.append([cr-1,cc,c_move+1])
# #             visited[cr-1][cc] = 1
# #
# #         if 0 <= cr + 1 < N and 0 <= cc < N and arr[cr+1][cc] <= cur_size and visited[cr+1][cc]==0:
# #             q.append([cr+1,cc,c_move+1])
# #             visited[cr+1][cc] = 1





#---------------------------------------------------------------------------------------
dr = [-1, 0, 0, 1] # 상 좌 우 하
dc = [0, -1, 1, 0]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N) ]

count = [0]*7  # 물고기 개수
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            sr = r
            sc = c
        elif arr[r][c] in [1,2,3,4,5,6]:
            count[arr[r][c]] += 1

# bfs로 물고기 찾기
# 자신보다 큰 물고기 인 곳은 못지나감
# 최단 거리인 후보군들 만들기
# 만약 후보군 없다면 엄마에게 돌아가기
# 정렬한 후, 이동하기
# c_size update

# 다시 위 과정 반복

def bfs(s_move, sr, sc, s_size, s_eat):

    visited = [[0]*(N) for _ in range(N)]
    visited[sr][sc] = 1
    # 물고기 먹으면0 으로 처리
    arr[sr][sc] = 0

    # 크기 초기화
    s_eat  += 1
    if s_eat == s_size:
        s_size += 1
        s_eat = 0

    q = [[sr, sc, s_size, s_eat, s_move]]


    candi = []
    cur_min_move = 0xffffff
    while q:
        cr, cc, c_size, c_eat, c_move = q.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 범위 내에 있고, 방문하지 않았고, 이동 가능한 크기인 경우
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] <= c_size and c_move+1 <= cur_min_move:
                q.append([nr, nc, c_size, c_eat, c_move + 1])

                if 0< arr[nr][nc] < c_size:
                    candi.append([c_move+1, nr, nc, c_size, c_eat])  # 거리 가깝고, 위쪽, 왼쪽에 있는 것 순으로 먹기위해
                    candi.sort()
                    cur_min_move = candi[0][0]

                visited[nr][nc] = 1


    # 더 이상 먹을 것이 없음
    if not candi:
        return s_move

    else:
        candi.sort()
        return candi[0]


s_size = 2
s_eat = -1
s_move = 0

result = [s_move, sr, sc, s_size, s_eat]
while type(result)!=int:
    result = bfs(*result)

print(result)







