
N, M = map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(N)]

coords = []
for r in range(N):
    for c in range(M):
        coords.append((r,c))


# 이동 / 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

from collections import deque

def get_num(lst):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    # q초기화
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2 and visited[i][j]==0:
                q.append([i,j])
                visited[i][j] = 1

                # q에 2인 것이 인다면, bfs 탐색 하기
                while q:
                    cr, cc = q.popleft()
                    for d in range(4):
                        nr = cr + dr[d]
                        nc = cc + dc[d]
                        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0 and visited[nr][nc]==0:
                            lst[nr][nc] = 2
                            visited[nr][nc]=1
                            q.append([nr,nc])

    # 결과로 0인것 개수 세기
    result = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                result +=1


    return result

from copy import deepcopy

# 3개 선택
cur_max = 0
length = len(coords)
for i in range(length):
    a1 = coords[i]
    for j in range(i+1,length):
        a2 = coords[j]
        for k in range(j+1, length):
            a3 = coords[k]


            if arr[a1[0]][a1[1]] == 0 and arr[a2[0]][a2[1]] == 0 and arr[a3[0]][a3[1]]==0:
                new = deepcopy(arr)
                new[a1[0]][a1[1]] = 1
                new[a2[0]][a2[1]] = 1
                new[a3[0]][a3[1]] = 1

                cur_num = get_num(new)

                if cur_num > cur_max:
                    cur_max = cur_num
print(cur_max)



