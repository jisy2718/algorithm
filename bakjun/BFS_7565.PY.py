import copy

# 1. input : 가로, 세로
M, N = map(int, input().split())

## 1: 익은토마토, 0: 안익은 토마토, -1 : 빈칸
arr = [list(map(int, input().split())) for _ in range(N)]

result = copy.deepcopy(arr)

visited = [[False] * M for _ in range(N)]

day = 0 # 숙성기간

# 익어야하는 토마토 개수
target = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            target += 1

# 현재 익힌 토마토 개수
count = 0

# 2. 이동규칙 : 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 3. 범위 내이고, visited False이고, 값이 0이면 이동하고 count += 1
while True:
    before_count = count
    for r in range(N):
        for c in range(M):
            # 조건이 맞다면 상하좌우 탐색
            if arr[r][c] == 1:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == False:
                        result[nr][nc] = 1  # result에 바꿔주기
                        # print(nr,nc)
                        count += 1
                        visited[nr][nc] = True
    #                     for row in arr:
    #                         print(row)
    #                     print('#--------------------')
    # for row in result:
    #     print(row)
    # print('#--------------------#')

    arr = copy.deepcopy(result)  # 다음 while 문 대비
    # 4. 만약 count가 변화가 없으면 break
    if before_count == count:
        break

    day += 1  # 하루가 지난 것


    # 목적만큼 익힌경우 day 반환 / 전부 익히지 못하면 -1 반환
if target == count:
    print(day)
else:
    print(-1)
