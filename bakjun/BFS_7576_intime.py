# import copy,sys
from collections import deque

# 1. input : 가로, 세로
M, N = map(int, input().split())

## 1: 익은토마토, 0: 안익은 토마토, -1 : 빈칸
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

# 2. 이동규칙 : 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 3. q로 한번 돌면서 1인 것 넣기 & 전체 목적 개수 세기
q = deque()
goal = 0  # 숙성시켜야하는 토마토 개수
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append([r, c])
            visited[r][c] = True
        elif arr[r][c] == 0:  # 몇 개의 토마토를 숙성시켜야 하는가
            goal += 1

# 4. while q
# n 주변의 것에 0있으면 넣기
result = 0

while q:
    # q에 있는 것들 모두 이동해서 숫자 올려서 다시 q에 넣기
    n = len(q)
    # for loop 1번 할 때마다 , 하루씩 지난다.
    for i in range(n):
        cr, cc = q.popleft()
        # 이동조건 만족 확인하기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 조건 만족하면 방문하고 q에 넣자
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == False:
                arr[nr][nc] = 1
                visited[nr][nc] = True
                goal -= 1  # 1개 숙성될때마다 목표를 달성해가자

                q.append([nr, nc])
    #print(f'cur q is {q}, cur result is {result}')

    # 만약 숙성된 것이 있다면 == q에 원소가 있다면
    if q:
        result += 1  # 숙성일수

if goal == 0:  # 목표달성
    print(result)
else:
    print(-1)

