import sys
sys.stdin = open("2382_input.txt")

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # 셀의 수 N , 격리시간 M, 군집개수 K

    arr = [[[0,0]]*N for _ in range(N)]


    # 상하좌우를 나타냄
    change_d = {}
    change_d[1] = 2
    change_d[2] = 1
    change_d[3] = 4
    change_d[4] = 3

    # 상하좌우가 arr에서 움직이는 방향
    move_d = {}
    move_d[1] = (-1,0)
    move_d[2] = (1,0)
    move_d[3] = (0,-1)
    move_d[4] = (0,1)


    for _ in range(K):
        r, c, nums, direct = map(int,input().split())  # direct 1 2 3 4 / 상하좌우
        arr[r][c] = [nums,direct]


    for _ in range(M):
        # 움직이기
        stack = []
        for r in range(N):
            for c in range(N):
                group = arr[r][c]
                if group != [0,0]:
                    loc = [r,c]

                    loc.extend(group)
                    # print('group',loc)
                    stack.append(loc)
                    # print('stack',stack)

        # 움직인 것 새로 저장하기
        arr = [[[0, 0]] * N for _ in range(N)]

        max_num = {}
        while stack:
            r, c, nums, direct = stack.pop()
            nr = r + move_d[direct][0]
            nc = c + move_d[direct][1]

            # 이미 있는 경우 어떻게 합쳐질지 고민
            if arr[nr][nc] != [0,0]:
                # 기존 max 가 더 큰 경우
                if max_num[(nr,nc)] > nums:
                    direct = arr[nr][nc][1]

                else: # 새로운 nums가 더 큰 경우
                    max_num[(nr,nc)] = nums
                arr[nr][nc] = [arr[nr][nc][0]+nums, direct]




            else:
                arr[nr][nc] = [nums, direct]
                max_num[(nr,nc)] = nums


            # 끝에 닿는 경우
            if nr <= 0 or nr >= N-1 or nc <=0 or nc >= N-1:
                arr[nr][nc] = [nums//2,change_d[direct]]


    result = 0
    for r in range(N):
        for c in range(N):
            result += arr[r][c][0]

    print(f"#{tc} {result}")