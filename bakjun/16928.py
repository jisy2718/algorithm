N, M = map(int,input().split()) # 사다리수, 뱀의 수

# 이동 규칙이 있는 판
game = {x : x for x in range(1,101)}

for _ in range(N+M):
    s, e = map(int,input().split())
    game[s] = e # s칸에 가면 e 칸으로 이동


# BFS
from collections import deque

visited = [0]*101
visited[0] = 1

q = deque()
q.append([1,0])
visited[1] = 1

while q:
    cur_loc, cur_cnt = q.popleft()

    if cur_loc == 100:
        print(cur_cnt)
        break

    for num in range(1,7):
        if 1<= cur_loc + num < 101:
            moved =game[cur_loc+num]
            if 1<= moved < 101 and visited[moved] == 0 :
                visited[moved] = 1
                q.append([moved, cur_cnt+1])


