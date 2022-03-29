import sys
sys.stdin = open("2819_input.txt")

T = int(input())

# 이동방향 / 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            # BFS로 path 길이가 7이 될 때까지 탐색
            path = [arr[r][c]]
            distance = 1
            queue = [[r, c, distance, path]]

            while True :
                cr, cc , cdistance, cpath = queue.pop(0)
                if cdistance == 7:
                    queue.append([cr,cc,cdistance,cpath])
                    break

                for i in range(4):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if 0 <= nr <4 and 0 <= nc <4 :
                        curpath = cpath[:]
                        curpath.append(arr[nr][nc])
                        queue.append([nr,nc,cdistance+1,curpath])

            # q에는 path가 길이 7인 것만 들어 있음/ 그렇지만 확실히 하기 위해, 길이 7인 것들 선별
            for res in queue:
                if res[2] == 7:
                    # print(res[3])
                    result.add(tuple(res[3]))


    print(f'#{tc} {len(result)}')
