import sys
sys.stdin = open('2105_input.txt')

# 이동규칙(좌하, 우하, 우상, 좌상)
dr = [1,1,-1,-1]
dc = [-1,1,1,-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = set()
    for r in range(N):
        for c in range(N):
            queue = [[r,c,[arr[r][c]],0]]

            while queue:
                # print('11',queue, r, c)
                cr , cc , path, direction = queue.pop(0)

                nr = cr + dr[direction]
                nc = cc + dc[direction]


                if nr == r and nc == c:
                    result.add(len(path))
                    # print(path)

                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in path:
                        cr , cc = nr, nc
                        cpath = path[:]
                        cpath.append(arr[cr][cc])
                        # 다음 방향 2가지 추가
                        queue.append([cr, cc, cpath,direction])
                        if direction != 3:
                            queue.append([cr,cc,cpath,direction+1])

    if result:
        print(f'#{tc} {max(result)}')
    else:
        print(f'#{tc} -1')

    #
    #         while queue:
    #             print(f'111cur  and queue is {queue}')
    #             cr, cc, path, direction = queue.pop(0)
    #             nr = cr + dr[direction]
    #             nc = cc + dc[direction]
    #             # while로 이동문 구현
    #             while 0 <= nr < N and 0 <= nc < N:
    #                cpath = path[:]
    #                print(f'222 cr, cc is {cr}, {cc}')
    #                print(f'2222 c, r is {c} {r}')
    #
    #                # 올바른 경로인 경우
    #                if nr != r and nc != c and arr[nr][nc] not in path :
    #                    print(f'333 cr, cc is {cr}, {cc}')
    #                    cpath.append(arr[cr][cc])
    #                    queue.append([cr,cc,cpath,direction+1])
    #                    nr = cr + dr[direction]
    #                    nc = cc + dc[direction]
    #                    # if direction != 3:
    #                    #      queue.append([cr,cc,cpath,direction+1])
    #                    # else:
    #                    #     queue.append([cr, cc, cpath, direction])
    #
    #                # 도착한경우
    #                elif cr == r and cc == c:
    #                    result.add(len(cpath))
    #
    #
    #                #올바르지 않은 경로인 경우
    #                else:
    #                    break
    #             print(f'cur directionis {direction} and queue is {queue}')
    # if result:
    #     print(f'#{tc} {max(result)}')
    # else:
    #     print(f'#{tc} -1')
    #
    #









    # dr의 순서에 따라 반복해서 움직이기
    # while queue:
    #     cr, cc, path, direction = queue.pop(0)
    #     nr = cr + dr[direction]
    #     nc = cc + dc[direction]
    # while로 이동문 구현
    #     while 0 <= nr < N and 0 <= nc < N:
    #        cr , cc = nr, nc
    #        cpath = path[:]
    #        if cr != r and cc != c and arr[cr][cc] not in path:  #올바른 경로인 경우
    #            cpath.append(arr[cr][cc])
    #            nr = cr + dr[i]
    #            nc = cc + dc[i]
    #            queue.append([cr,cc,cpath,direction+1])
    # 도착한경우
    #        elif cr == r and cc == c:
    #            result.add(len(cpath))
    #
    # 올바르지 않은 경로인 경우
    #        else:
    #            break
