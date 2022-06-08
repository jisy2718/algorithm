# dfs 시간초과------------------------------------------------------------
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N)  ]

    max_prob = 0
    used= [0]*N
    def dfs(idx, cur_prob):
        global max_prob
        if max_prob >= cur_prob:
            return

        if idx == N:
            if max_prob < cur_prob:
                max_prob = cur_prob

        else:
            for i in range(N):
                if used[i] == 0:
                    used[i] = 1
                    dfs(idx+1, cur_prob*(arr[i][idx]/100))
                    used[i] = 0

    dfs(0,1)
    print(f'#{tc}{round(max_prob*100,6) : .6f}')


#
# #----DP---------------------------------------------------------
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [ list(map(int,input().split())) for _ in range(N)  ]
#
#     max_prob = 0
#
#     def dfs(idx, selected):
#         if dp[selected]:
#             return dp[selected]
#
#         else:
#
#
#
#
#     print(f'#{tc}{round(max_prob*100,6) : .6f}')
