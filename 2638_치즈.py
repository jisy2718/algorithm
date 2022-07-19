


# 외부 공기를 -1로 코딩
# 내부 공기는 그대로 0
# 치즈는 1

# 매 번 치즈가 없어질 때마다, 외부공기를 update


N , M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]


# 치즈의 크기
size = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            size += 1


# (0,0) 은 무조건 외부공기 이므로, 여기부터 외부공기 모두 찾기
from collections import deque
# 바깥 공기를 -1로 update
def update_outside_air():

    q = deque()
    q.append([0,0])
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    while q:
        cr, cc = q.popleft()
        arr[cr][cc] = -1

        for move in [[0,1],[1,0],[-1,0],[0,-1]]:
            nr = cr + move[0]
            nc = cc + move[1]
            if 0 <= nr < N and 0<= nc < M and visited[nr][nc] == 0 and arr[nr][nc] in [-1,0] :
                q.append([nr,nc])
                visited[nr][nc] = 1

def remove_cheese():
    global size
    def check(cr,cc):
        count = 0 # 공기와 접촉면 개수
        for move in [[0,1],[1,0],[-1,0],[0,-1]]:
            nr = cr + move[0]
            nc = cc + move[1]
            if 0 <= nr < N and 0<= nc < M and arr[nr][nc]==-1:
                count += 1
        # 제거할 치즈
        if count >=2:
            return True
        # 제거되지 않는 치즈
        return False

    # 전체 공간 탐색
    removed = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                if check(r,c):
                    removed.append([r,c])
                    size -= 1

    for rc in removed:
        r,c = rc
        arr[r][c] = -1

answer = 0
while size > 0:
    update_outside_air()
    remove_cheese()
    answer += 1

print(answer)


