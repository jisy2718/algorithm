def find_cost(r,cur_cost):
    # 마지막줄까지 비용합친경우
    global min_cost
    global used_col
    if r == N:
        if min_cost > cur_cost:
            min_cost = cur_cost

    else:
        if cur_cost < min_cost: # promising
            for c in range(N):
                if used_col[c] == 0:
                    used_col[c] = 1  # c열 사용해서 함수 다시 실행
                    find_cost(r+1,cur_cost+arr[r][c])
                    used_col[c] = 0  # c열 사용하지 않은 채로, 다음 loop 에서 이용할 c 찾기


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_cost = 15* 99
    used_col = [0]*N
    find_cost(r=0,cur_cost=0)

    print(f"#{tc} {min_cost}")

