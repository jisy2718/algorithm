# 1인곳에서 0인곳들을 팔방으로 전염시키는 문제와 같은 문제

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

visited = [[-1]*M for _ in range(N)]

# 이동 12 1,3,...
dr = [-1, -1, 0 ,1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

zero = 0
queue = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            zero += 1
        else:
            queue.append([r,c,0])
            visited[r][c] = 0


result = 1
while queue:
    cr, cc , cd = queue.pop(0)

    for i in range(8):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
            queue.append([nr, nc, cd+1])
            visited[nr][nc] = cd + 1
            zero -= 1

            if zero == 0:
                result = cd + 1
                break

print(result)

