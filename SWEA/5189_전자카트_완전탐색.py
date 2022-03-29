import sys
sys.stdin = open('5189_input.txt')

#
# def dfs(before, cur, cur_elec, visited):
#     global min_elec
#     cur_elec += arr[before][cur]
#     print(f"{before} to {cur} , 현재전기소비량 {cur_elec}")
#
#     if sum(visited)==N:
#         last = cur_elec + arr[cur][1]
#         if min_elec > last:
#             min_elec = last
#
#     else:
#         for i in range(1,N+1):
#             if visited[i] == False:
#                 visited[i] = True
#                 next_loc = i
#                 dfs(cur,next_loc,cur_elec,visited)
#
def perm(idx, N):
    global min_elec
    if idx == N:
        cur_elec = 0
        new = [1] + p + [1]
        # print(new)
        for i in range(len(new)-1):
            cur_elec += arr[new[i]][new[i+1]]
            # print(arr[i][i+1])
        if cur_elec < min_elec:
            min_elec = cur_elec
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[idx] = a[i]
                perm(idx+1, N)
                used[i] = 0
    return




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 행 : 출발지, 열 : 도착지, arr 값 : 전기 소비량
    arr = [[0]*(N+1)] + [[0]+ list(map(int,input().split())) for _ in range(N)]

    min_elec = 1000000
    a = list(range(2, N + 1))
    p = [0] * (N - 1)
    used = [0] * (N - 1)
    perm(0, N - 1)


    print(f"#{tc} {min_elec}")


