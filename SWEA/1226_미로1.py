import sys
sys.stdin = open('1226_input.txt')
T = 10
N = 16
for tc in range(1, T + 1):
    # 1. input & result
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0

    # 2. 이동 규칙 (상우하좌)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    # 3. visited & stack
    visited = [[False] * N for _ in range(N)]
    stack = []

    # 4. 출발/ 도착 찾기
    sr = sc = 0  # 출발(행,열)
    er = ec = 0  # 도착(행,열)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j


    stack.append([sr,sc])
    while stack:
        topr, topc = stack[-1]


        for i in range(4):
            nr = topr + dr[i]
            nc = topc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc]==0 and visited[nr][nc]==False:
                stack.append([nr,nc]) # append가 방문
                visited[nr][nc] = True
                break

            # 종료
            if maze[nr][nc] == 3:
                result = 1
                while stack:  # 밖의 while 빠져나가기 위해
                    stack.pop()
                break

        else:
            stack.pop() # 현재 top 에서는 더이상 갈 곳이 없음

    print(f"#{tc} {result}")