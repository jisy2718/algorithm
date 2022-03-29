import sys
sys.stdin = open('1861_input.txt')
# 방 Aij 는 1~ N**2 중복없이 NxN
# 이동은 상하좌우 & 자신보다 1큰 곳으로만 이동가능

# 처음에 어디서 시작해야 가장 많이 이동 가능한가?


# DFS 경로 모두 찾으면 됨.
# 이동규칙 & 조건을 +1, -1로 주고 visited로 해서 최대 단지 찾으면 됨
# 그리고 거기서 최소인 수 찾으면 됨. (-1 인 곳으로 더이상 못가는 부분 찾기)

T = int(input())
for tc in range(1,T+1):
    # 1. input 받기 & visited 생성
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 2. 이동규칙 / 상우하좌
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    # 3. DFS
    max_volumn = 0
    min_loc = [0,0]
    min_value = N**2
    for r in range(N):
        for c in range(N):
            # VISITED 안된 곳에서 무조건 시작
            if visited[r][c] == False:
                visited[r][c] = True
                stack = [[r,c]]
                cur_volumn = 1
                cur_value = arr[r][c]
                # DFS 시작
                while stack:
                    cr, cc = stack[-1]

                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]

                        if 0 <= nr < N and 0 <= nc < N and (visited[nr][nc] == False) and ( (arr[nr][nc] == arr[cr][cc] - 1) or (arr[nr][nc] == arr[cr][cc] + 1)):
                            cur_volumn += 1
                            stack.append([nr,nc])
                            visited[nr][nc] = True
                            if arr[nr][nc] < cur_value:

                                cur_value = arr[nr][nc]

                            break
                    else:
                        stack.pop()
                if cur_volumn > max_volumn:
                    max_volumn = cur_volumn
                    min_value = cur_value
                elif cur_volumn == max_volumn and cur_value < min_value:
                    min_value = cur_value


    print(f'#{tc} {min_value} {max_volumn}')