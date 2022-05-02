#----------------------------------------------------dfs 시간초과--------------------------------
# N = int(input())
# stairs = [0]  # 시작지점
# for _ in range(N):
#     stair = int(input())
#     stairs.append(stair)
#
# stairs = tuple(stairs)
#
#
# def dfs(cur, before, total_score):  # before : 1칸 전 계단 올라왔는지 여부
#     global max_score
#     if cur > N:
#         return
#
#     if cur == N:
#         total_score += stairs[N]
#         if max_score < total_score:
#             max_score = total_score
#             return
#     else:
#         if before == True:  # 1칸 전 계단을 올라왔다면, 2칸 가야함
#             dfs(cur + 2, before=False, total_score=total_score + stairs[cur])
#
#         else:
#             dfs(cur + 1, before=True, total_score=total_score + stairs[cur])
#             dfs(cur + 2, before=False, total_score=total_score + stairs[cur])
#
#
# max_score = 0
# dfs(0, False, 0)
# print(max_score)
#--------------------------------------------------------------------------------


#--------------------------DP-----------------------------------------------------
N = int(input())
stairs = [0]  # 시작지점
for _ in range(N):
    stair = int(input())
    stairs.append(stair)

stairs = tuple(stairs)
scores = [[0]*(N+1) for _ in range(3)]  # 1행은 1칸 전에서 온 경우 # 2행은 2칸 전에서 온 경우 최대 값

if N == 1:
    print(stairs[N])
elif N ==2 :
    print(stairs[1]+stairs[2])
elif N >=3:

    # n-1 번째 칸을, 1칸 건너서 온 경우(n-1_1)와 2칸 건너서 온 경우(n-1_2)
    # n-2 번째 칸을, 1 칸 건너서 온 경우(n-2_1)와 2칸 건너서 온 경우(n-2_2)

    # n 번째 위치에 올 수 있는 경우의 수는 n-1_2 에서 1칸 오는 경우 or (n-2_1, n-2_2)에서 2칸 오는 경우
    # 따라서 n_1 = n-1_2 + stairs[n]
    #        n_2 = max(n-2_1, n-2_2) + stairs[n]
    # 초기값은 생각해보면, 아래와 같음.
    scores[1][1] = stairs[1]
    scores[1][2] = stairs[1] + stairs[2]
    scores[2][2] = stairs[2]
    for i in range(3, N+1):
        scores[1][i] = scores[2][i-1] + stairs[i]
        scores[2][i] = max(scores[2][i-2], scores[1][i-2]) + stairs[i]


    print(max(scores[1][N], scores[2][N]))




