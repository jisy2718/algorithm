import sys
sys.stdin = open('2117_input.txt')
from pprint import pprint
# K 의크기는 대각선을 다 덮을만큼만 하면 됨
# 가로,세로,대각선은 2K-1 길이임

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # N이 홀수면 K = 1,...,N 까지
    # N이 짝수면 K = 1,...,N, N + 1 까지
    if N%2==1:
        K = N
    else:
        K = N+1


    max_benefit_cost = 0
    max_house = 0
    for r in range(N):
        for c in range(N):

            # if arr[r][c] == 1:
            #     benefit += M
            # 모든 이동가능 경로
            for k in range(1,K+1): # 1 ~ K 까지 해봐야함
                # print(f"k is {k}-----------------------------------------------------")
                benefit = 0
                cost = k**2 + (k-1)**2 if k > 1 else 1  # K**2 + (K-1)**2 when K > 1

                dr = [0]
                dc = [0]
                for t in range(1,k+1):
                    up_dr = list(range(-1,-t,-1)) # 1 ~ K-1 까지 인데 (-)
                    up_dc = list(range(t-2,-1,-1)) # K-2 ~ 0 까지

                    right_dr = list(range(t-2,-1,-1)) # K-2 ~ 0 칸이동
                    right_dc = list(range(1,t))  # 1 ~ K-1 칸 이동

                    down_dr = list(range(1,t)) # 1 ~ K-1 칸 칸 이동
                    down_dc = list(range(-(t-2),1)) # K-2 ~ 0칸 이동  (-)

                    left_dr = list(range(-(t-2),1))     # K-2 ~ 0 칸 이동 (-)
                    left_dc = list(range(-1,-t,-1)) # 1 ~ K-1 칸 이동 (-)

                    dr = dr + up_dr + right_dr + down_dr + left_dr
                    dc = dc + up_dc + right_dc + down_dc + left_dc

                # visited = [[0]*N for _ in range(N)]
                for d in range(len(dr)):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <=nc < N and arr[nr][nc]==1:
                        # print(f"r,c ,k= {r} {c} {k} / nr,nc = {nr} {nc}")
                        benefit += M

                    # if 0 <= nr < N and 0 <= nc < N:
                    #     print(nr,nc)
                    #     visited[nr][nc] = 1
                # print(f"r,c = {r} {c}, k = {k}")
                # pprint(visited)

                if 0 <= benefit - cost and max_house < benefit/M:
                    max_house = benefit/M
                    # print(f"cur max is r, c, k =  {r} {c} {k} / benefit-cost = {benefit-cost}, house ={benefit/M}")
    print(f"#{tc} {int(max_house)}")





