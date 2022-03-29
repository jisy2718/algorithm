import sys
sys.stdin = open('4875_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

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

    # 5. 이동하기
    stack.append((sr, sc))
    visited[sr][sc] = True
    result = 0
    while stack:
        cr, cc = stack[-1]  # 현재 위치

        # 이동
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] == 0:  # 방문가능 조건
                visited[nr][nc] = True  # 방문
                stack.append((nr, nc))
                break
            elif 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == 3:  # 도착성공
                result = 1  # 결과 표시
                while stack:
                    stack.pop()  # break 후에 밖의 while 문 빠져나가기 위해
                break
        else:
            stack.pop()  # break 안일어나면 경로나 도착지를 못찾은 것이므로 pop

    # while 문 탈출 후에, result 인쇄
    print(f'#{tc} {result}')

