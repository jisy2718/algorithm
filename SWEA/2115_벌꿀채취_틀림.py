import sys
# sys.stdin = open("2117_input.txt")

def find_max(i , m, result, benefit):
    # print(i,m,result)
    if result > C and m > M:
        return

    if m == 2*M and result <= C:
        if same_row_result[i] < benefit:
            same_row_result[i] = benefit

    elif m <= M and result <= C:
        if results[i] < benefit:
            results[i] = benefit

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            find_max(i,m+1,result+arr[i][j],benefit+ arr[i][j]**2)
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):

    # N : NxN 벌통 배열, M : 한 행에서 채취할 수 있는 벌통 개수(벌통단위로만 채취), C : 한 행에서 최대채취 가능 양
    N, M, C = map(int,input().strip().split())  # 각 벌통의 꿀의 양은 1~9 /  N >= M
    same_row_result = [0]*N
    arr = [list(map(int,input().split())) for _ in range(N)]
    results= [0]*N
    visited = [0]*N
    # 각 행별로 최대 채취 가능량 계산하면 됨
    for i in range(N):
        cur_max = 0
        find_max(i,0,0,0)

    print(results ,same_row_result)

    max_amount = max(results[0],results[1])
    second_amount = min(results[0],results[1])
    for i in range(2,N):
        if results[i] >= max_amount:
            second_amount = max_amount
            max_amount = results[i]

        elif second_amount < results[i] < max_amount:
            second_amount = results[i]

    final_result = max_amount+second_amount
    for i in range(N):
        if same_row_result[i] > final_result:
            final_result = same_row_result[i]

    print(f"#{tc} {final_result}") # 제곱수

#
# #--------------------------------------------------
#
# def find_max(benefit):
#     global first
#     global second
#
#     if benefit >= first:
#         second = first
#         first = benefit
#     elif first > benefit > second:
#         second = benefit
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     # N : NxN 벌통 배열, M : 한 행에서 채취할 수 있는 벌통 개수(벌통단위로만 채취), C : 한 행에서 최대채취 가능 양
#     N, M, C = map(int,input().split()) # 각 벌통의 꿀의 양은 1~9 /  N >= M
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # memoization 이용
#     memo = [[0]*N for _ in range(N)]
#     # 각 행에 대해서 M개를 연속해서 탐색, 시작하는 열의 index는 0 ~ N - M
#     # (i,j) 위치에는 , [채취할 수 있는 양,benefit] 을 입력
#
#     for i in range(N):
#         for j in range(N):
#             col_move = 0 # 이동횟수로, 0 ~ M-1 까지 값 가짐
#             amount = 0   # 꿀의 양
#             benefit = 0
#             # j + col_move 는 index 범위 내에 있어야 하고,
#             while j + col_move < N and col_move < M:
#
#                 amount += arr[i][j+col_move]
#                 benefit += (arr[i][j+col_move])**2
#
#
#                 if amount > C:
#                     benefit -= (arr[i][j+col_move])**2
#                     break
#
#                 col_move += 1
#
#             memo[i][j] = benefit
#             # find_max(benefit)  # max와 second max 값 찾기
#     for row in memo:
#         print(row)
#
#     # 한 줄에서 2명이 채취하는 경우
#     ans = 0
#     for i1 in range(N):
#         for j1 in range(N-M+1):
#             ans1 = memo[i1][j1]
#             # move = memo[i1][j1][0]  # 총 move 칸 만큼 채취
#             j2 = j1 + M
#             while j2 <= N-M:
#                 ans2 = memo[i1][j2]
#                 if ans < ans1 + ans2:
#                     ans = ans1 + ans2
#                 j2 += 1
#
#
#
#     # 한 줄에서 1명 씩만 채취하는 경우
#     first = second = 0
#     for i in range(N):
#         cur_max = memo[i][0]
#         for j in range(N):
#             if memo[i][j] > cur_max:
#                 cur_max = memo[i][j]
#         find_max(cur_max)
#
#     print(first, second)
#     ans = max(ans, first+second)
#     print(f"#{tc} {ans}")
#
#
#
#
#
#
