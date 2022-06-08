# import sys
# sys.setrecursionlimit(10**6)
#
#
# N = int(input())
# colors_T = [ list(map(int,input().split()))  for _ in range(N)]
# colors = [ tuple(color) for color in zip(*colors_T) ]
#
# r, g, b = colors
#
#
# def dfs(idx, color, cost):   # 현재 색칠되어 있는 idx 와 color, cost
#     global min_cost
#     if idx == N-1:
#         if min_cost > cost:
#             min_cost = cost
#
#     if cost >= min_cost:
#         return
#
#     else:
#         for next_color in colors:
#             if next_color != color:
#                 next_cost = cost + next_color[idx+1]
#                 dfs(idx+1, next_color, next_cost)  # idx+1 번째까지 계산된 값
#
#
# min_cost = 0xffffffffff
# dfs(-1,0,0)
# print(min_cost)
#--------------------------------------------------------------



# DP 이용

N = int(input())
colors_T = [ list(map(int,input().split()))  for _ in range(N)]
colors = [ tuple(color) for color in zip(*colors_T) ]

r, g, b = colors

costs = [[0]*N for _ in range(3)]
rc, gc, bc = costs   # i번째 집에 각 색을 칠한 경우에 도달할 수 있는 최소 cost

rc[0] = r[0]
gc[0] = g[0]
bc[0] = b[0]


for i in range(1,N):
    rc[i] = min( gc[i-1]  , bc[i-1] ) + r[i]

    gc[i] =  min( rc[i - 1] ,  bc[i - 1] ) + g[i]


    bc[i] = min( gc[i - 1], rc[i - 1]) + b[i]


print(min(rc[-1],gc[-1],bc[-1]))
