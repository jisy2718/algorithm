
T = int(input())
for tc in range(1,T+1):
    N = int(input())

    T = [list(map(int,input().split())) for _ in range(N)]

    cur_min_end = 0
    next_min_end = 24

    result = 0
    while True:
        flag = False
        for t in T:
            ts ,te = t
            if cur_min_end <= ts and next_min_end >= te: # 시작 가능하고 가장 빨리 끝남
                next_min_end = te
                flag = True

        else: # 더이상 작업 불가
            if flag == False:
                break


        if flag == True:
            result += 1
            cur_min_end = next_min_end
            next_min_end = 24

    print(f"#{tc} {result}")





